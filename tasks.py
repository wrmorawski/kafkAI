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
