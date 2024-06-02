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


SHORT_CHAPTER_SUMMARY_PRMOPT = Prompt(
    name = 'scsp',
    description = 'This is the multi-role prompt with previous and next chapters summary.',
    prompt= [
      {
        'role': 'system',
        'content': "Write in the literary style of Franz Kafka"   
      },
      {
        'role': 'user',
        'content': "Generate a missing fragments of Kafka's novel The Trial. In the unfinished chapter's Josef K. decides to dismiss his lawyer, Herr Huld, \
          despite attempts from the lawyer, Leni, and another client, Block, to dissuade him. K. confronts the lawyer, learns about Leni's peculiar attraction to accused men, and witnesses the lawyer's control over Block.\
          The next chapter K. is tasked with escorting an influential Italian client, but the client doesn't show up. At the cathedral, K. encounters the prison chaplain"
      }
    ]
)

#system with lenght. Get the mean length of chapters. 



# SYS_KAFKA = "Write in the style of Franz Kafka"

# Maybe generate what happens in those chapters.    

# next, add sys prompts 

# Write the mean number of characters for each chapter in Kafka's novel The Trial. 