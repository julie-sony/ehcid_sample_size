import os
import sys
import argparse
from utils import utils 
from core import do_eval

def get_opt():
    # This method gets and returns command line arguments. 
    parser = argparse.ArgumentParser()    
    
    # Get task/model pair.
    parser.add_argument('--task_model', type=str, default='pose_movenet',
                        help='Input as task/model selection as task_model, e.g. --task_model pose_movenet')      
    # Get data directory. 
    parser.add_argument('--data_dir', type=str, default='/home/julienne/Documents/sample_size/COCO_Val_2014/',
                        help='Path to directory containing EHCID data.')                             
    # Get save directory. 
    parser.add_argument('--save_dir', type=str, default='./out/',
                        help='Output directory where to save CSV files containing accuracy data.')    

    # Parse and return args.                     
    opt = parser.parse_args()
    opt.data_dir = os.path.abspath(opt.data_dir) # Convert data path to an absolute path. 
    opt.save_dir = os.path.abspath(opt.save_dir) # Convert save path to an absolute path. 
    return opt

def main():
    # Get command line argument values. 
    opt = get_opt()
    
    # If save directory does not exist, create it 
    utils.ensure_dir(opt.save_dir)
    
    print('Running inference and evaluating: ' + opt.task_model)
    # Run the process on the task/model. 
    do_eval.run(opt.task_model, opt.data_dir, opt.save_dir)

if __name__ == '__main__':
    main()
    
    
    
    

