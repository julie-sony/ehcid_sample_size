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
    N_factor_min = 275
    N_factor_max = 325
    N_factors = np.arange(N_factor_min, N_factor_max, 5)
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
        i = rows['group1']
        j = rows['group2']

        if(i != "Male_Dark" or j != "Male_Light"):
            continue

        
        if(original_data):
            df_pair = df[(df['group'] == i) | (df['group'] == j)]

        else: 
            df_i = df[(df['group'] == str(i))]
            df_j = df[(df['group'] == str(j))]

            min_sample_size = min(len(df_i), len(df_j))

            df_i_unified = df_i.sample(n = 50* (min_sample_size // 50), replace = False, random_state = 123)
            df_j_unified = df_j.sample(n = 50* (min_sample_size // 50), replace = False, random_state = 123)

        for f in N_factors:
            print('Bootstrapping for groups: {}, {} and ratio {}, '.format(i, j, f))

            counter_low = 0
            counter_high = 0

            for seed in range(B2): 
                if(int(f*len(df_i_unified)) < len(df_i)):
                    df_i_upsampled = df_i.sample(n = int(f*len(df_i_unified)), replace = False, random_state = seed)
                else: 
                    df_i_upsampled = df_i.sample(n = int(f*len(df_i_unified)), replace = True, random_state = seed)

                if(int(f*len(df_j_unified)) < len(df_j)):
                    df_j_upsampled = df_j.sample(n = int(f*len(df_j_unified)), replace = False, random_state = seed)
                else: 
                    df_j_upsampled = df_j.sample(n = int(f*len(df_j_unified)), replace = True, random_state = seed)
                
                df_upsampled = pd.concat([df_i_upsampled, df_j_upsampled])

                group_i = df_upsampled[(df_upsampled['group'] == str(i))] 
                group_j = df_upsampled[(df_upsampled['group'] == str(j))] 

                # perform bootstrapping 
                acc_i = group_i['acc'].tolist()
                acc_j = group_j['acc'].tolist()

                # convert array to sequence
                acc = (acc_i, acc_j)

                if(len(acc_i) >= 50 and len(acc_j) >= 50): 
                    # Calculate 95% bootstrapped confidence interval for median
                    total_bootstrap_ci = bootstrap(acc, difference_in_mean, confidence_level = 0.95, n_resamples = B1, \
                                                   method = 'basic', vectorized = False)
                    if(total_bootstrap_ci.confidence_interval[0] > -tolerance/2): 
                        counter_low += 1
                    if(total_bootstrap_ci.confidence_interval[1] < tolerance/2):
                        counter_high += 1
                else:
                    continue
                    #counter_low = -1 
                    #counter_high = -1 

            ci = total_bootstrap_ci.confidence_interval
            avg = difference_in_mean(acc_i, acc_j)
            tmp = {'group1': str(i), 'group2' : str(j), 'N1': len(group_i), 'N2': len(group_j),'frac':f, 'pi_low':counter_low/B2, 'pi_high':counter_high/B2, 'ci_low': ci[0], 'ci_high': ci[1], 'obs_diff':avg}
            row = pd.DataFrame(tmp, index = [0])
            results = pd.concat([results, row], ignore_index = True)

            if(counter_low/B2 > 0.95 and counter_high/B2 > 0.95):
                break

    save_data_path = save_dir + '/' + task_model + '_power_results_' + p_groups + '.csv'
    results.to_csv(save_data_path, index = False)
