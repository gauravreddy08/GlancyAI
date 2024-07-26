from YoutubeHelper import get_transcript
from dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from LLM import LLM


class Database():
    def __init__(self, data):
        load_dotenv()
        self.embeddings = OpenAIEmbeddings()

        self._build_RAG(data)

    def _build_RAG(self, data):
        docs = [
            Document(
                page_content = get_transcript(video_id)
                ) for video_id in data['id']
            ]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        all_splits = text_splitter.split_documents(docs)

        self.db = Chroma.from_documents(documents=all_splits, embedding=self.embeddings)
    
    def retrieve(self, query, k=10):
        agent = LLM(model_name='gpt-4o-mini')
        enchanced_query = agent.call(query, tool_choice='required')
        docs = self.db.similarity_search(query=enchanced_query, k=k)
        if docs:
            return "\n".join(doc.page_content for doc in docs)
        else: 
            return ""





        
        
            