import os
import sys
import argparse
from utils import utils 
from core import do_eval, do_bootstrapping_eval


def get_opt():
    # This method gets and returns command line arguments. 
    parser = argparse.ArgumentParser()    
    
    # Get path to accuracy results data.
    parser.add_argument('--acc_path', type=str, default='./out/fake_pose_movenet_results.csv',
                        help='Input path to task/model accuracy value CSV')
    # Get process type (e.g. bootstrapping, plotting, other statistical analysis).                     
    parser.add_argument('--run_type', type=str, default='do_bootstrapping',
                        help='Input which type of evaluation to perform; e.g. --run_type do_bootstrapping')                    
    # Get save directory. 
    parser.add_argument('--save_dir', type=str, default='./out',
                        help='Input directory where to save plots and output files.')    
    # Parse and return args.                     
    opt = parser.parse_args()
    opt.acc_path = os.path.abspath(opt.acc_path) # Convert save path to an absolute path. 
    opt.save_dir = os.path.abspath(opt.save_dir) # Convert save path to an absolute path. 
    return opt

def main():
    # Get command line argument values. 
    opt = get_opt()
    print('Beginning process: ' + opt.run_type)
    
    # If save directory does not exist, create it 
    utils.ensure_dir(opt.save_dir)
    
    # This is where we will call code to do bootstrapping, statistical analysis, and plotting code. 
    
    

if __name__ == '__main__':
    main()
    
    
