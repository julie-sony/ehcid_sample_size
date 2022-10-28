import os
import sys
import pandas as pd

def ensure_dir(file1_path, file2_path):
    '''If a directory at file1_path does not exist, create it.'''
    directory = os.path.dirname(file1_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    '''If a directory at file_path does not exist, create it.'''
    directory = os.path.dirname(file2_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_json(fpath):
    with open(fpath) as f:
        data = json.load(f)
    return data


def add_attribute_columns(acc_path, attribute_path):

    df = pd.read_csv(acc_path, names = ['image_file', 'acc'])

    meta = pd.read_csv(attribute_path)
    meta.rename(columns = {'Unnamed: 0' : 'image_file'}, inplace = True)

    df = df.merge(meta, on = 'image_file')
    #df['group'] = df[group]
    df.to_csv(acc_path.replace('.csv','_modified.csv'))


