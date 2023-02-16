import os
import sys
import argparse
from utils import utils 
from core import do_eval, do_bootstrapping, do_poweranalysis


def get_opt():
    # This method gets and returns command line arguments. 
    parser = argparse.ArgumentParser()    
    
    # Get task/model pair.
    parser.add_argument('--task_model', type=str, default='pose_movenet',
                        help='Input as task/model selection as task_model, e.g. --task_model pose_movenet')      
    # Get path to accuracy results data.
    parser.add_argument('--acc_path', type=str,
                        help='Input path to task/model accuracy value CSV')

    # Get path to the attribute file 
    parser.add_argument('--attribute_path', type=str, default='./meta_data/instances_2014.csv',
                        help='Input path to image meta data CSV')
  
    # Get process type (e.g. bootstrapping, plotting, other statistical analysis).                     
    parser.add_argument('--run_type', type=str, default='do_bootstrapping',
                        help='Input which type of evaluation to perform; e.g. --run_type do_bootstrapping')                    
    # Get save directory. 
    parser.add_argument('--save_dir', type=str, default='./out',
                        help='Input directory where to save plots and output files.')    

    # Get protected groups. It asks for two groups. If one group is desired, pass '' as the last argument
    # Example: python main_stats.py --p_groups 'skin_color' ''
    parser.add_argument('--p_groups', nargs = 2, type=str, default='sex',
                        help ='Group with fairness consideration.')   

    # Parse and return args.                     
    opt = parser.parse_args()
    opt.acc_path = os.path.abspath(opt.acc_path) # Convert save path to an absolute path. 
    opt.attribute_path = os.path.abspath(opt.attribute_path) # Convert save path to an absolute path. 
    opt.save_dir = os.path.abspath(opt.save_dir) # Convert save path to an absolute path. 
    return opt

def main():
    # Get command line argument values. 
    opt = get_opt()
    print('Beginning process: ' + opt.run_type)
    
    # If save directory does not exist, create it 
    utils.ensure_dir(opt.acc_path, opt.attribute_path)
    
    # select the dataset 
    if('coco' in opt.acc_path):
        dataset = 'coco'

    if('synthesisai' in opt.acc_path):
        dataset = 'synthesisai'
        
    # add the attribute column
    utils.add_attribute_columns(opt.acc_path, opt.attribute_path, dataset)
    opt.acc_path = opt.acc_path.replace('.csv','_modified.csv')

    if(opt.run_type == 'do_bootstrapping'):
        # This is where we will call code to do bootstrapping
        do_bootstrapping.run(opt.task_model, opt.acc_path, opt.save_dir, opt.p_groups)

    if(opt.run_type == 'do_poweranalysis'):
        # This is where we will call code to do power analysis
        do_poweranalysis.run(opt.task_model, opt.acc_path, opt.save_dir, opt.p_groups)

    if(opt.run_type == 'do_plotting'):
        # This is where we will call code to do plotting 
        pass
    
if __name__ == '__main__':
    main()
    
    
