from invoke import task
import os 

@task
def remove_pycache(ctx):
    print("Removing __pycache__ directories...")
    os.system("rm -rf */__pycache__")
    os.system("rm -rf __pycache__")