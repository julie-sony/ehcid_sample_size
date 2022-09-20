import os
import sys
import pandas as pd
from scipy.stats import bootstrap


def read_input(acc_path):
    df = pd.read_csv(acc_path)
    return df 

def run(task_model, acc_path, save_dir):
    print('*** bootstrapping running ***')

    bootstrap_results = {}

    df = read_input()
    acc = df['acc'].tolist()
    
    # convert array to sequence
    acc = (acc,)

    # calculate 95% bootstrapped confidence interval for median
    total_bootstrap_ci = bootstrap(acc, np.median, confidence_level=0.95,
                            random_state=1, method='percentile')

    bootstrap_results['total'] = total_bootstrap_ci.confidence_interval

    # number of distinct social groups 
    groups = df['group'].unique()

    # perform group-wise bootstrapping
    for i in groups:
        
        # subset the data 
        group_df = df.loc[df['group'] == i]

        # perform bootstrapping 
        group_acc = group_df['acc'].tolist()
        
        # convert array to sequence
        group_acc = (group_acc,)

        # calculate 95% bootstrapped confidence interval for median
        group_bootstrap_ci= bootstrap(group_acc, np.median, confidence_level=0.95,
                                random_state=1, method='percentile')
        bootstrap_results[str(group)] = group_bootstrap_ci.confidence_interval


    save_data_path = save_dir + '/' + task_model + '_bootsrapping_results.csv'
    with open(save_data_path, 'w') as f:
        writer = csv.writer(f)
        for key, value in bootstrap_results.items():     
            # randomly generate output. Note: random int at the end is an indicator of group membership          
            row = str(key) + ',' + str(value)   
            writer.writerow([row])
    
    
