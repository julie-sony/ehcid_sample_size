import os
import sys

def ensure_dir(file_path):
    '''If a directory at file_path does not exist, create it.'''
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_json(fpath):
    with open(fpath) as f:
        data = json.load(f)
    return data
