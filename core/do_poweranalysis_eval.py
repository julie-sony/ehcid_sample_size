import os
import sys
import pandas as pd
import numpy as np
import random
import itertools
from scipy.stats import bootstrap

def read_input(acc_path):
    df = pd.read_csv(acc_path)
    return df 

'''
def run(task_model, acc_path, save_dir):
    print('*** power analysis running ***')

    tolerance = 0.01        # acceptable disparities must be in [-tolerance, tolerance]
    N_factor_min = 1.25
    N_factor_max = 1.75
    B = 1000                # number of draws for bootstrapping 
    N_factors = np.arange(N_factor_min, N_factor_max, 0.25)
    results = pd.DataFrame(columns=('groups','N','frac','pi_low','pi_high'))   

    df = read_input(acc_path)
    group_pairs = list(itertools.combinations(df['group'].unique(), 2))    

    for (i, j) in group_pairs:
        for f in N_factors:
            counter_low = 0
            counter_up = 0
            df_pair = df[(df['group'] == i) | (df['group'] == j)]

            # Bootstrapping analysis 
            for seed in range(B): 
                df_upsampled = df_pair.sample(frac = f, replace = True, random_state = seed)

                acc = df_upsampled['acc'].tolist()
                acc = (acc,)

                # Calculate 95% bootstrapped confidence interval for median
                total_bootstrap_ci = bootstrap(acc, np.mean, confidence_level = 0.95, n_resamples = B)
                
                if(total_bootstrap_ci.confidence_interval[0] < -tolerance):
                    counter_low += 1
                if(total_bootstrap_ci.confidence_interval[1] > tolerance):
                    counter_up += 1

            tmp = {'groups':(i, j), 'N':int(f*len(df_pair)), 'frac':f, 'pi_low':counter_low/B, 'pi_high':counter_up/B}
            row = pd.Series(tmp)
            results = pd.concat([results, row.to_frame().T], axis = 0, ignore_index=True)

    save_data_path = save_dir + '/' + task_model + '_power_results.csv'
    results.to_csv(save_data_path, index = False)
'''


def read_test_input():
    acc_path = '/Users/aidarahmattalabi/Dropbox/SonyAI-Full/Projects/EHCID/SampleSize/ehcid_sample_size/data/test.csv'
    df = pd.read_csv(acc_path)

    df['acc'] = (df['New'] - df['Approved'])/(df['Approved'] - df['Placebo'])
    df['group'] = np.random.randint(1, 3, len(df))
    return df 

def difference_in_mean(x, y):
    
    diff = [i - j for (i, j) in zip(x, y)]
    # res = list(df.groupby('group')['acc'].mean())
    # diff = res[0] - res[1]

    return sum(diff)/len(diff) 

def run(task_model, acc_path, save_dir):
    print('*** power analysis running ***')

    tolerance = 0.2        # acceptable disparities must be in [-tolerance, tolerance]
    N_factor_min = 1.25
    N_factor_max = 1.26
    B = 1000                # number of draws for bootstrapping 
    N_factors = np.arange(N_factor_min, N_factor_max, 0.25)
    results = pd.DataFrame(columns=('groups','N','frac','pi_low','pi_high'))   

    df = read_input(acc_path)
    group_pairs = list(itertools.combinations(df['group'].unique(), 2))    

    for (i, j) in group_pairs:
        for f in N_factors:
            counter_low = 0
            counter_up = 0
            for seed in range(B): 
                df_pair = df[(df['group'] == i) | (df['group'] == j)]
                df_upsampled = df_pair.sample(frac = f, replace = True, random_state = seed)

                acc = df_upsampled['acc'].tolist()
                acc = (acc,)

                # Calculate 95% bootstrapped confidence interval for median
                total_bootstrap_ci = bootstrap(acc, np.mean, confidence_level = 0.90, n_resamples = B)
                
                if(total_bootstrap_ci.confidence_interval[0] < -tolerance):
                    counter_low += 1
                if(total_bootstrap_ci.confidence_interval[1] > tolerance):
                    counter_up += 1

            tmp = {'groups':(i, j), 'N':int(f*len(df_pair)), 'frac':f, 'pi_low':counter_low/B, 'pi_high':counter_up/B}
            row = pd.Series(tmp)
            results = results.append(row, ignore_index = True)

    return results

