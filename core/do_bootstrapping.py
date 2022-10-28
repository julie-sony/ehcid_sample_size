import os
import sys
import csv
import pandas as pd
import numpy as np
import itertools
from itertools import product
from scipy.stats import bootstrap

def difference_in_mean(x, y):
    diff = sum(x)/len(x) - sum(y)/len(y)
    return diff

def run(task_model, acc_path, save_dir, p_groups):
    print('*** bootstrapping running ***')

    df = pd.read_csv(acc_path)

    if(p_groups[1] == ''): #single group
        df['group'] = df[p_groups[0]]
        p_groups = p_groups[0]
    else:
        df['group'] = df[p_groups[0]].astype(str) + '_' + df[p_groups[1]].astype(str)
        p_groups = p_groups[0] + '_' + p_groups[1]

    group_pairs = list(itertools.combinations(df['group'].unique(), 2))  

    B = 1000   
    tolerance = 0.02             
    results = pd.DataFrame(columns=('group1', 'group2', 'N1', 'N2','low','high','width','obs_diff','zero_included'))   
    groups = pd.DataFrame(columns=('group1', 'group2'))   

    # perform bootstrapping to find confidence interval around the mean difference
    for (i, j) in group_pairs:
        # subset the data 
        group_i = df[(df['group'] == i)] 
        group_j = df[(df['group'] == j)] 

        # perform bootstrapping 
        acc_i = group_i['acc'].tolist()
        acc_j = group_j['acc'].tolist()

        # convert array to sequence
        acc = (acc_i, acc_j)

        # calculate 95% bootstrapped confidence interval for mean
        bootstrap_ci = bootstrap(acc, difference_in_mean, confidence_level = 0.95, n_resamples = B,\
                                 method = 'basic', vectorized = False)
    
        ci = bootstrap_ci.confidence_interval
        obs_diff = difference_in_mean(acc_i, acc_j)

        if(ci[0] < 0 and ci[1] > 0):    
            zero_included = True
        else:   
            zero_included =  False

        width = ci[1] - ci[0]

        tmp = {'group1': str(i), 'group2' : str(j), 'N1' : len(acc_i), 'N2' : len(acc_j), 'low': ci[0], 'high': ci[1], 'width' : width, \
               'obs_diff' : obs_diff, 'zero_included' : zero_included}

        row = pd.DataFrame(tmp, index = [0])
        results = pd.concat([results, row], ignore_index = True)

        if width >= tolerance and zero_included:
            groups = pd.concat([groups, pd.DataFrame({'group1' : i, 'group2' : j}, index = [0])], ignore_index = True)

    save_data_path = save_dir + '/' + task_model + '_bootsrapping_results_'+ p_groups +'.csv'
    save_groups_path = save_dir + '/' + task_model + '_' + p_groups + '.csv'

    results.to_csv(save_data_path, index = False)
    groups.to_csv(save_groups_path, index = False)
    
