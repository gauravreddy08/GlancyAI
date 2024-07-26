from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, List
import json

class LLM():
    def __init__(self, model_name='gpt-4o', system=None, db=None):
        load_dotenv()
        self.model = OpenAI()
        self.model_name = model_name
        self.db = db

        self.messages = []

        if system:
            self._append('system', system)
        
        f = open('./config/agent.json', 'r')
        self.tools = json.load(f)

    def call(self, prompt: str, tool_choice='none'):

        self._append('user', prompt)
        
        if self.db:
            retrieved_info = self.db.retrieve(prompt)
            self._update(retrieved_info)


        completion = self.model.chat.completions.create(
                        model=self.model_name,
                        messages=self.messages,
                        tools = self.tools,
                        tool_choice=tool_choice
                    )
        
        tool_calls = completion.choices[0].message.tool_calls
        
        if tool_calls:
            for tool_call in tool_calls:
                function_args = json.loads(tool_call.function.arguments)
                return function_args.get("query")
                
        self._append('assistant', str(completion.choices[0].message.content))

        return self.messages[-1]['content']
    
    def _append(self, role: str, content: str):
        self.messages.append({'role': role,
                              'content': str(content)})
    
    def _update(self, content):
        self.messages[-1]['content'] = "\n" + content

