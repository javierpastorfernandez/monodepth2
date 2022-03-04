#!/usr/bin/env python3

"""
Created on Fri Mar  4 10:04:49 2022
@author: Javier Pastor Fernández
"""

"""
print("----- IMPORTING SEARCH OF DIRECTORIES --------")
import sys
print(sys.path)

#Listing the name of the modules
print(dir())
"""

# -----------------------------------------------------------------------------------------------
# Import dependencies
import os 
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tifffile  import imread
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.axes_grid1 import ImageGrid

from monodepth2.scared_utils import *

# Set global parameters
verbose=True


# Set main paths for data accessing
base_dir=os. getcwd()
dataset_root_dir='/media/datasets/biomedical_datasets/SCARED/unzipped'
dataset_num=1 
keyframe=1
frame_data_dir=dataset_root_dir+'/dataset_'+str(dataset_num)+'/keyframe_'+str(keyframe)+'/data/frame_data'
scene_points_dir=dataset_root_dir+'/dataset_'+str(dataset_num)+'/keyframe_'+str(keyframe)+'/data/scene_points'
image_num=1
image_path=scene_points_dir+'/scene_points'+'{0:06}'.format(image_num)+'.tiff'

#scene_points000001.tiff
if verbose:
    # Current directory is /home/jpastor
    print("Base directory: ",base_dir)
    print("Dataset root directory: ",dataset_root_dir)
    print("Frame data directory: ",frame_data_dir)
    print("Scene points directory: ",scene_points_dir)
    print("Image path directory: ",image_path)



fig=plt.figure(figsize=(8, 6), dpi=80)

img_list=list()
for i in range (0,7):
    image_num=i
    image_path=scene_points_dir+'/scene_points'+'{0:06}'.format(image_num)+'.tiff'
    img = imread(image_path)
    image_analizer(img)
    img_norm=image_normalizer(img,3)
    img_list.append(img_norm)

grid_plot(img_list,fig,len(img_list))



# Reading an 
# OpenCV is not capable of reading scene_points tiff files (32-bits samples)



