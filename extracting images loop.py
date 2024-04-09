# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 16:04:22 2024

@author: Marit
"""

from PIL import Image
import os

# Base path where the images are located
base_path = 'C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\'

# Dimensions and positions for the squares
square_size = (97, 97)
column_starts = [8, 116, 301, 409]  # Starts for columns 1 and 2 of sets 1 and 2 respectively
row_starts = [6, 114, 222]  # Starts for rows 1, 2, and 3
border_size = 2  # Size of the border around each square

columns = 2
rows = 3
sets = 2

# Loop through the range of images
for i in range(1, 100):  # Assuming file names are 'BP_1' to 'BP_99'
    # Construct the full path of the image
    image_name = f'p0{i}.gif'
    original_image_path = os.path.join(base_path, image_name)
    original_image = Image.open(original_image_path)
    
    # Loop through each set, column, and row to extract and save the images
    for set_id in range(1, sets + 1):
        for col_num in range(1, columns + 1):
            for row_num in range(1, rows + 1):
                # Calculate the bounding box of the square using the provided positions
                left = column_starts[(set_id - 1) * 2 + (col_num - 1)]
                upper = row_starts[row_num - 1]
                right = left + square_size[0]
                lower = upper + square_size[1]

                # Extract the square image
                square_image = original_image.crop((left, upper, right, lower))

                # Create a new image with a black border
                bordered_image = Image.new('RGB', (square_image.width + 2 * border_size, square_image.height + 2 * border_size), 'black')
                bordered_image.paste(square_image, (border_size, border_size))

                # Save the image with the proper naming convention
                filename = f'p0{i}_{set_id}_{col_num}_{row_num}.png'  # Removing '.gif' from image name
                save_path = os.path.join(base_path, filename)
                bordered_image.save(save_path)