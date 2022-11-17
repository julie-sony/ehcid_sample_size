import os
import sys
import pandas as pd
import numpy as np
import random
import itertools
from scipy.stats import bootstrap

def difference_in_mean(x, y):
    diff = sum(x)/len(x) - sum(y)/len(y)
    return diff

def run(task_model, acc_path, save_dir, p_groups):
    print('*** power analysis running ***')

    B1 = 1000                # number of draws for bootstrapping 
    B2 = 100
    tolerance = 0.02         # acceptable disparities must be in [-tolerance, tolerance]
    N_factor_min = 1
    N_factor_max = 5.5
    N_factors = np.arange(N_factor_min, N_factor_max, 0.5)
    results = pd.DataFrame(columns=('group1','group2','N1','N2','frac','pi_low','pi_high','low','high','avg'))   
    original_data = False    # use original data or make the samples equal for faster power analyses 

    df = pd.read_csv(acc_path)

    if(p_groups[1] == ''): #single group
        df['group'] = df[p_groups[0]]
        p_groups = p_groups[0]
    else:
        df['group'] = df[p_groups[0]].astype(str) + '_' + df[p_groups[1]].astype(str)
        p_groups = p_groups[0] + '_' + p_groups[1]

    group_pairs = pd.read_csv(save_dir + '/' + task_model + '_' + p_groups + '.csv')


    for index, rows in group_pairs.iterrows():
        for f in N_factors:
            i = rows['group1']
            j = rows['group2']

            if(original_data):
                df_pair = df[(df['group'] == i) | (df['group'] == j)]

            else: 
                df_i = df[(df['group'] == i)]
                df_j = df[(df['group'] == j)]

                min_sample_size = min(len(df_i), len(df_j))

                df_i = df_i.sample(n = 50* (min_sample_size // 50), replace = False, random_state = 123)
                df_j = df_j.sample(n = 50* (min_sample_size // 50), replace = False, random_state = 123)

            counter_low = 0
            counter_up = 0

            print('Bootstrapping for groups: {}, {} and ratio {}, '.format(i, j, f))
            for seed in range(B2): 
                
                df_i_upsampled = df_i.sample(n = int(f*len(df_i)), replace = True, random_state = seed)
                df_j_upsampled = df_j.sample(n = int(f*len(df_j)), replace = True, random_state = seed)
                
                df_upsampled = pd.concat([df_i_upsampled, df_j_upsampled])

                group_i = df_upsampled[(df_upsampled['group'] == i)] 
                group_j = df_upsampled[(df_upsampled['group'] == j)] 

                # perform bootstrapping 
                acc_i = group_i['acc'].tolist()
                acc_j = group_j['acc'].tolist()

                # convert array to sequence
                acc = (acc_i, acc_j)
                if(len(acc_i) > 1 and len(acc_j) > 1): 
                    # Calculate 95% bootstrapped confidence interval for median
                    total_bootstrap_ci = bootstrap(acc, difference_in_mean, confidence_level = 0.95, n_resamples = B1, \
                                                   method = 'basic', vectorized = False)
                    if(total_bootstrap_ci.confidence_interval[0] < -tolerance/2):
                        counter_low += 1
                    if(total_bootstrap_ci.confidence_interval[1] > tolerance/2):
                        counter_up += 1
                else:
                    counter_low = -1 
                    counter_up = -1 

            ci = total_bootstrap_ci.confidence_interval
            avg = difference_in_mean(acc_i, acc_j)
            tmp = {'group1': str(i), 'group2' : str(j), 'N1': len(group_i), 'N2': len(group_j),'frac':f, 'pi_low':counter_low/B2, 'pi_high':counter_up/B2, 'ci_low': ci[0], 'ci_high': ci[1], 'obs_diff':avg}
            row = pd.DataFrame(tmp, index = [0])
            results = pd.concat([results, row], ignore_index = True)

    save_data_path = save_dir + '/' + task_model + '_power_results_' + p_groups + '.csv'
    results.to_csv(save_data_path, index = False)
