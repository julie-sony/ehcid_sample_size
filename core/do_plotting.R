rm(list=ls())
library(tidyverse)
library(ggplot2)

my_theme = theme(
  axis.title.x = element_text(size = 16, family = "Times"),
  axis.text.x = element_text(size = 14, family = "Times"),
  axis.title.y = element_text(size = 16, family = "Times"),
  axis.text.y = element_text(size = 16, family = "Times"),
  legend.title=element_text(size=16, family = "Times"),
  legend.text =element_text(size=16, family = "Times"))

groups = c('skin_color','sex','illumination_intensity',
           'skin_color_illumination_intensity', 'skin_color_sex',
           'illumination_intensity_sex')

for(group in groups)
{
  file = paste0('pose_movenet_power_results_', group,'.csv') 
  pathname = '/Users/aidarahmattalabi/Dropbox/SonyAI-Full/Projects/EHCID/SampleSize/ehcid_sample_size/results/'
  
  
  df <- read.csv(file = paste0(pathname, file))
  
  df <- df %>% mutate(group = paste0(group, ': ',group1,',',group2))
  
  pd <- position_dodge(0.1) # move them .05 to the left and right
  
  p <- df %>% ggplot(aes(x = N1, y = avg)) + 
         geom_point() + 
         geom_errorbar(aes(ymin = low, ymax = high), width = 0.3, position = pd) + 
         facet_wrap('group') + my_theme + 
          ylab('disparity') + xlab('N') + theme(strip.text = element_text(size = 14, family = "Times"))

  pathname = '/Users/aidarahmattalabi/Dropbox/SonyAI-Full/Projects/EHCID/SampleSize/ehcid_sample_size/visualize/'
  file = paste0(group,'.pdf') 
  ggsave(paste0(pathname, file), p, width = 25, height = 20)
} 
