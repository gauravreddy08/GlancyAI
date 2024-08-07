from src.LLM import LLM
from src.PromptParser import PromptParser
from src.YoutubeHelper import search
from src.Data import Data
from src.RAG import Database

def main():
    prompt = PromptParser()
    ini_llm = LLM(system=prompt.get('youtube_query'))

    user_input = input("> User: ")
    query = ini_llm.call(user_input)

    results_dict = search(query, max_results=50)

    data = Data(results_dict)
    data.filter(count=10, min_latest=5)
    database = Database(data.data)

    llm = LLM(db=database)
    while True:
        user_input = input("> User: ")
        if user_input=='q': break
        output = llm.call(user_input)
        print(f"> Assitant: {output}")



if __name__ == '__main__':
    main()