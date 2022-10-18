import os
import sys
import numpy as np
import csv

def run(data_dir, save_dir):
    print('Analyzing MoveNet.')

    print('Saving fake test data for stats analysis')
    
    # Generate normal distribution of points: 
    mu0, sigma0, mu1, sigma1 = 0, 0.1, 0.005, 0.1 # mean and standard deviation
    s0 = np.random.normal(mu0, sigma0, 50)
    s1 = np.random.normal(mu1, sigma1, 50)

    s = np.concatenate((s0, s1), axis = 0)
    save_data_path = save_dir + '/fake_pose_movenet_results.csv'
    with open(save_data_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['image_file', 'acc', 'group'])
        for i in range(len(s)): 

            # randomly generate output. Note: random int at the end is an indicator of group membership  
            if(i < 50):        
                row = ['fake_img_' + str(i).zfill(3) + '.png', str(s[i]), str(0)]   
            else: 
                row = ['fake_img_' + str(i).zfill(3) + '.png', str(s[i]), str(1)]   

            writer.writerow(row)
    
    
