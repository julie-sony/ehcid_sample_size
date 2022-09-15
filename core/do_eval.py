import os
import sys
from models import pose_movenet

# Here is where data can be loaded in a consistent format for feeding into various models. 

def run(task_model, data_dir, save_dir):
    print('Performing basic evaluation.')
    
    if(task_model == 'pose_movenet'):
        pose_movenet.run(data_dir, save_dir)

    
