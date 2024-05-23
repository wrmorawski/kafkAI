from scripts.generate_ollama import get_responses
from prompts.prompts import MOST_BASIC_PROMPT
from utils.maintenance import check_runtime

models = ['llama2', 'llama3', 'mistral']
prompts =[MOST_BASIC_PROMPT]

get_responses(models, prompts)