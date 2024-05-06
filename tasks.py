from invoke import task
import os 
from utils.maintenance import clear_test_outputs

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
