class Prompt: 
    
    prompts = {}

    def __init__(self, name: str, description: str, prompt: str) -> None:
        self.name = name
        self.description = description
        self.prompt = prompt
        Prompt.prompts[self.name] = self

    def __str__(self) -> str:
        return f"Name: {self.name}\nDescription: {self.description}"
    
    @classmethod
    def get_prompt(cls, name):
        return cls.prompts.get(name)

MOST_BASIC_PROMPT = Prompt(
    name = 'mbp',
    description = 'This is a most basic prompt for the task.',
    prompt= [
      {
        'role': 'user',
        'content': "Generate a missing chapter for Kafka's novel The Trial"
      },
    ]
)

# SYS_KAFKA = "Write in the style of Franz Kafka"

# Maybe generate what happens in those chapters.    

# next, add sys prompts 

# Write the mean number of characters for each chapter in Kafka's novel The Trial. 