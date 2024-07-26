from LLM import LLM
from PromptParser import PromptParser
from YoutubeHelper import search
from Data import Data
from RAG import Database

import streamlit as st

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

    st.session_state.llm = None

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Message GlancyAI"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    if not st.session_state.llm:
        with st.chat_message('assistant'):
            with st.status("Processing..."):
                st.write("Analysing Requirements...")
                prompt_parser = PromptParser()
                ini_llm = LLM(system=prompt_parser.get('youtube_query'))
                query = ini_llm.call(prompt, tool_choice='required')

                st.write(f"Searching YouTube ({query})...")

                results_dict = search(query, max_results=50)

                st.write(f"Retrieved {len(results_dict)} videos from YouTube.")

                data = Data(results_dict)
                data.filter(count=10, min_latest=5)

                st.write(f"Builing Vector Space (acquired {len(data.data)})...")

                database = Database(data.data)

                st.write(f"Powering up the LLM...")

                st.session_state.llm = LLM(db=database)

                st.markdown("Ask away!")
    
    else:
        response = st.session_state.llm.call(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})




