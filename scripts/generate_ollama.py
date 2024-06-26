"""This module generates output for LLMs using ollama library."""
import ollama

from utils.logger import configure_logger
from utils.save_to_file import save_to_pdf
from utils.maintenance import check_runtime
from prompts.prompts import Prompt

logger = configure_logger(__name__)

def get_responses(models: list[str], prompts: list[str], stream=False) -> None:
    """This function generates response for many models and messages and saves it to a PDF file."""
    for model in models:
        for prompt_name in prompts:
            prompt = Prompt.get_prompt(prompt_name)
            
            logger.info(f'Model: {model} \nPrompt: {prompt.name}')
            try: 
                get_single_ai_response_and_save_it(model, prompt, stream=stream)
            except Exception as e:
                logger.error(f"Skipping item due to an unexpected error: {e}")

@check_runtime
def get_single_ai_response_and_save_it(model_id, message, stream: bool) -> None:
  """This function generates response from a signle user prompt and saves it to a PDF file.
  
    Args:
        model_id (str): The model id to use for generating response.
        message (dict): A dictionary containing the user prompt. 
        For prompt example see: README file. 
  """
  # Get response
  logger.info('Getting response...')
  response = ollama.chat(model=model_id, messages=message.prompt, stream=stream)

  if stream:
    for chunk in response:
      print(chunk['message']['content'], end='', flush=True)
    return

  # Save response to PDF
  logger.info('Saving response to PDF...')
  text = f'model: {model_id}\n created_at: {response["created_at"]}\n prompt: {message.prompt[0]["content"]}\n\n response: \n {response["message"]["content"]}' 
  
  filename = f'{message.name}_{model_id}_{response["created_at"]}.pdf' 
  
  save_to_pdf(text, filename)


#TODO move try error to get_single.. function 