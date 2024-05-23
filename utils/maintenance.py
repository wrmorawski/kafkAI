import os 
import time 

from utils.constants import OUTPUT_PATH

def clear_test_outputs():
    for file in os.listdir('./outputs'):
        if file.startswith('test_'):
            os.remove(os.path.join(OUTPUT_PATH, file))


def check_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' took {runtime:.6f} seconds ( {runtime/60:.2f} minutes) to run.")
        return result
    return wrapper

