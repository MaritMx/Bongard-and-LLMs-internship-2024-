# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:19:35 2024

@author: Marit
"""

import os
from PIL import Image

def split_images(folder_path):
    # Navigate through each file in the directory
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct full file path
            file_path = os.path.join(folder_path, filename)
            # Open the image
            with Image.open(file_path) as img:
                width, height = img.size
                
                # Define the splitting point
                mid_point = width // 2
                
                # Left half
                left = img.crop((0, 0, mid_point, height))
                left_file_path = os.path.join(save_path_left, filename.replace('.', '_left.'))
                left.save(left_file_path)
                
                # Right half
                right = img.crop((mid_point, 0, width, height))
                right_file_path = os.path.join(save_path_right, filename.replace('.', '_right.'))
                right.save(right_file_path)

# Provide the full path to the folder containing the images
folder_path = r'C:\Users\Marit\Downloads\Documenten UvA\ResMas\Internship\Bongard problems\MC_variations'
save_path_left = r'C:\Users\Marit\Downloads\Documenten UvA\ResMas\Internship\Bongard problems\MC_variations\left'
save_path_right = r'C:\Users\Marit\Downloads\Documenten UvA\ResMas\Internship\Bongard problems\MC_variations\right'


split_images(folder_path)
