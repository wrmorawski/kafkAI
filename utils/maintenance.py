import os 

from utils.constants import OUTPUT_PATH

def clear_test_outputs():
    for file in os.listdir('./outputs'):
        if file.startswith('test_'):
            os.remove(os.path.join(OUTPUT_PATH, file))

