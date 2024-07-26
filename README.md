![GlancyAI](assets/GlancyAI.gif)

Being viewed as the tech guy is a lot of fun, don't get me wrong. Sometimes it gets frustrating to explain to your friends that you cannot hack their ex's Facebook account. However, there is something more frustrating, which is when people ask you about which smartphone, laptop, or headphones to buy.

Honestly, when I need to buy something myself, I'm often mostly clueless. I stumble across articles, ***[YouTube videos]()***, and finally make an ***[educated wish]()*** to buy a certain product. However, your friends don't understand this; they expect you to know every chip, every smartphone and its six different configs, and all the headphones on the market and all the junk.

So for us (the tech people), and for all humanity, I introduce **GlancyAI**.

> ## What is GlancyAI?
> 
> **TL;DR:** GlancyAI is an LLM (like ChatGPT) that you can talk with, and it recommends products and helps you make your educated guess to buy a product.

## How is GlancyAI different from GPT?

One lesson I learned while building AI solutions is to think about how a human would do that particular task. 

For instance, I am heavily dependent on YouTube videos whenever I have to make an educated guess to buy a product. Well, GlancyAI does the same. 

Whenever a user asks for anything, let's say "I wanna buy a laptop under $1000," it intelligently queries YouTube and gets information on all the current standings of the products. After that, GlancyAI becomes knowledgeable about all the products on the market, and you can ask all your questions to make ***[your own educated wish]()*** to buy a product.

## So Is it just Another RAG Application?

> Well yes, and also no. 

See, my target audience for this application is non-tech guys who know nothing about prompt engineering, few-shot learning, zero-shot learning, or anything. So I made GlancyAI as easy to use as possible. 

Users can chat with it like they would with a friend, and no matter what they say, even if it's semantically imperfect, the ***[agents]()*** under the hood fixes it.

## Agents? What Agents?

> This isn't just a RAG-backed LLM. 

The system is backed by agents. Whenever a user asks anything, the LLM doesn't just query YouTube; it does so intelligently, backed by agents, to get the most appropriate results. And also, whenever a user asks questions, it restructures the user's query in a way to get the best results from RAG.

In an agentic RAG, agents are used to orchestrate and manage the various components of the RAG pipeline, as well as to perform additional tasks and reasoning that go beyond simple information retrieval and generation.

> Finally, I did this all for you, so that you, the non-tech person, don't have to think twice when trying to research a product.

Sure, here's the updated content:

## What's Under the Hood?

GlancyAI uses GPT-4o for the main LLM that users interact with and GPT-4o mini as an agent to make decisions on structuring queries.

### Structure of Files

- `app.py`: Runs the Streamlit application.
- `main.py`: Runs the app via the command line.
- `src`: Contains all necessary files and source code.
- `config`: Contains tools for function calling and prompts needed for the LLM to function.

To run the application, use:
```sh
streamlit run app.py
```

## Future Developments and Updates

The app is nowhere near perfect. Here are some future improvements:

1. **YouTube Transcripts**: Not all YouTube videos have transcripts, so I need to use something like Whisper to handle this case.
2. **YouTube Fetching Reliability**: The current package used to fetch YouTube videos is unreliable, sometimes fetching 30 videos, sometimes only 2. I might need to replace it with something more reliable.
3. **Dynamic Agentic RAG**: The current Agentic RAG is good, but I need a Dynamic Agentic RAG. For instance, if the user asks about MacBooks, the RAG pipeline initializes to detect all YouTube videos on MacBooks. But if the user suddenly switches to ask about Chromepads, the LLM model is clueless, defeating the system's purpose. This can be fixed by implementing a Dynamic RAG.

## Contributing

We welcome contributions! If you have suggestions or want to report issues, please open an issue or submit a pull request.

