#!/bin/sh

# python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'skin_color' '';
# python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'sex' '';
# python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'illumination_intensity' '';
# python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'skin_color' 'sex';
# python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'skin_color' 'illumination_intensity';
# python main_stats.py --task_model 'pose_movenet' --acc_path './out/hrnet_synthesisai_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results' --p_group 'illumination_intensity' 'sex';



#python main_stats.py --task_model 'pose_hrformer' --acc_path './out/hrformer_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/hrformer_coco_pck0p5_results' --p_group 'skin_group' '';
#python main_stats.py --task_model 'pose_hrformer' --acc_path './out/hrformer_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/hrformer_coco_pck0p5_results' --p_group 'gender' '';
python main_stats.py --task_model 'pose_hrformer' --acc_path './out/hrformer_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/hrformer_coco_pck0p5_results' --p_group 'gender' 'skin_group';
# python main_stats.py --task_model 'pose_hrnet' --acc_path './out/hrnet_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/hrnet_coco_pck0p5_results' --p_group 'skin' '';
# python main_stats.py --task_model 'pose_hrnet' --acc_path './out/hrnet_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/hrnet_coco_pck0p5_results' --p_group 'gender' '';
# python main_stats.py --task_model 'pose_hrnet' --acc_path './out/hrnet_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/hrnet_coco_pck0p5_results' --p_group 'skin_group' '';
# python main_stats.py --task_model 'pose_simplebaseline2d' --acc_path './out/simplebaseline2d_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/simplebaseline2d_coco_pck0p5_results' --p_group 'skin' '';
# python main_stats.py --task_model 'pose_simplebaseline2d' --acc_path './out/simplebaseline2d_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/simplebaseline2d_coco_pck0p5_results' --p_group 'gender' '';
# python main_stats.py --task_model 'pose_simplebaseline2d' --acc_path './out/simplebaseline2d_coco_pck0p5_results.csv' --run_type 'do_poweranalysis' --save_dir './results/simplebaseline2d_coco_pck0p5_results' --p_group 'skin_group' '';
