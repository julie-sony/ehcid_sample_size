import os
import sys
from models import pose_movenet

def run(save_dir):
    print('Performing basic evaluation.')
    
    pose_movenet.run(save_dir)

    
