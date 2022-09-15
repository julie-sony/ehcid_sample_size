import os
import sys
import numpy as np
import csv

def run(data_dir, save_dir):
    print('Analyzing MoveNet.')

    print('Saving fake test data for stats analysis')
    
    # Generate normal distribution of points: 
    mu, sigma = 0, 0.1 # mean and standard deviation
    s = np.random.normal(mu, sigma, 1000)
    
    save_data_path = save_dir + '/fake_pose_movenet_results.csv'
    with open(save_data_path, 'w') as f:
        writer = csv.writer(f)
        for i in range(len(s)):              
            row = 'fake_img_' + str(i).zfill(3) + '.png, ' + str(s[i])      
            writer.writerow([row])
    
    
