# kafkAI
Generate missing parts of Kafka's novels!

# Scope of the project 
In this project I want to generate the missing parts of Franz Kafka's novels (The Trial, The Castle and Amerika) using LLM models. 

# Limitations
Due to technical issues I decided to start with easily available models using ollama library and basic prompts. 
The next step will be the following: 
1. Use larger models 
2. Use openai API 
3. Finetune models 

# Other tasks: 
- find an easily readable format for output. 
- find the average number of words and characters for The Trial. 
- format outputs and convert to PDF 
- create architecture for saving prompts and models info 

# Models 
Mixtral 8x7B 


# Sources: 
https://www.cliffsnotes.com/literature/t/the-trial/critical-essays/structure-and-order-of-chapters-in-the-trial


# Usage 

## Prompt example: 
```
PROMPT_EXAMPLE = {
    'name': 'prompt_name',
    'description': 'This is a most basic prompt for the task.',
    'prompt': [
      {
        'role': 'user',
        'content': "Generate a missing chapter for Kafka's novel The Trial"
      },
    ]
}
```
