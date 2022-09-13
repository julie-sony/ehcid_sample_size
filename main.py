import os
import sys
import argparse
from utils import utils 
from core import do_eval, do_bootstrapping_eval


def get_opt():
    # This method gets and returns command line arguments. 
    parser = argparse.ArgumentParser()    
    
    # Get task/model pair.
    parser.add_argument('--task_model', type=str, default='pose_movenet',
                        help='Input as task/model selection as task_model, e.g. --task_model pose_movenet')
    # Get process type (e.g. basic evaluation vs. bootstrapping).                     
    parser.add_argument('--run_type', type=str, default='do_eval',
                        help='Input which type of evaluation to perform; e.g. --run_type do_eval or --run_type do_bootstrapping')                    
    # Get save directory. 
    parser.add_argument('--save_dir', type=str, default='./out',
                        help='Input directory where to save standard json and analysis files')    
    # Parse and return args.                     
    opt = parser.parse_args()
    opt.save_dir = os.path.abspath(opt.save_dir) # Convert save path to an absolute path. 
    return opt

def main():
    # Get command line argument values. 
    opt = get_opt()
    print('Beginning process: ' + opt.run_type + ' on ' + opt.task_model)
    
    # If save directory does not exist, create it 
    utils.ensure_dir(opt.save_dir)
    
    # Run the process on the task/model. 
    do_eval.run(opt.save_dir)

if __name__ == '__main__':
    main()
    

