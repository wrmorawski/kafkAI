from invoke import task
import os 
from utils.maintenance import clear_test_outputs
import toml 
from scripts.generate_ollama import get_responses
from prompts.prompts import MOST_BASIC_PROMPT

@task
def remove_pycache(ctx):
    print("Removing __pycache__ directories...")
    os.system("rm -rf */__pycache__")
    os.system("rm -rf __pycache__")


@task
def list_ollama_models(ctx): 
    ctx.run("ollama list")


@task 
def clear_outputs(ctx):
    pass 


@task 
def install_ollama_linux(ctx):
    ctx.run("curl -fsSL https://ollama.com/install.sh | sh")


@task 
def ollama_pull(ctx, models):
    # if more than one model then run inv ollama-pull "model1 model2 model3"
    for model in models.split():
        ctx.run(f"ollama pull {model}")


@task(optional=["file", "models", "prompts"],)
def ollama_generate(ctx, models=None, prompts=None, file=None):
    """"    
    Generates text for models

    optional file argument specifies .toml file with parameters

    example use: 
    a) inv ollama-generate -m tinyllama -p mbp 
    b) inv ollama-generate --file config.toml 
    """
    if file is not None: 
        #read_toml_file
        if not os.path.exists(file):
            print("File does not exist")
            return
        else: 
            #read all settings from toml file 
            pass
    else: 
        models_list = models.split()
        prompts_list = prompts.split()

    get_responses(models_list, prompts_list)
