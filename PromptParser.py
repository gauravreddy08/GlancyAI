import toml

class PromptParser():
    def __init__(self, filename='prompts.toml'):
        file = open(filename, 'r')
        self.data = toml.load(file)

    def get(self, key: str) -> str:
        if not key: return None
        return self.data[key]['prompt']
    

