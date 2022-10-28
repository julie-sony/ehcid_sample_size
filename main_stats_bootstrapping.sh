#!/bin/sh
#python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'sex'
#python main_stats.py --task_model 'pose_movenet' --acc_path './out/fake_pose_movenet_results.csv' --run_type 'do_bootstrapping' --save_dir './results' --p_group 'sex'
#python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_bootstrapping' --save_dir './results' --p_group 'sex';
#python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_bootstrapping' --save_dir './results' --p_group 'ancestry';
python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_bootstrapping' --save_dir './results' --p_group 'skin_color' 'sex' ;
python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_bootstrapping' --save_dir './results' --p_group 'skin_color' 'illumination_intensity'