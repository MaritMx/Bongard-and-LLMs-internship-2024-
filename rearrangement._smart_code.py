# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:55:17 2024

@author: Marit
"""

from PIL import Image
import os

# Parameters
columns = 2
rows = 3
image_count = columns * rows  # Total images per grid
grid_count = 2  # Number of grids
border_size = 10  # Border size between images
outer_border = 20  # Outer border size around the entire image
grid_spacing = 50  # Space between grids

# Load the extracted images (assuming they are named sequentially like 'BP_1_1_1.png')
extracted_image_paths = [
    f'p02_{set_id}_{col_num}_{row_num}.png'
    for set_id in range(1, grid_count + 1)
    for row_num in range(1, rows + 1)
    for col_num in range(1, columns + 1)
]

# Load images and get individual image dimensions
images = [Image.open(img_path) for img_path in extracted_image_paths]
img_width, img_height = images[0].size

# Adjusted calculations for side-by-side grids with outer borders and increased space between grids
total_width = (img_width * columns + border_size * (columns - 1)) * grid_count + grid_spacing + outer_border * 2
total_height = img_height * rows + border_size * (rows - 1) + outer_border * 2
new_image = Image.new('RGB', (total_width, total_height), 'white')


def create_and_save_image(version):
    # Create a new image for each version to reset its state
    new_image = Image.new('RGB', (total_width, total_height), 'white')

    for grid_num in range(grid_count):
        for row_num in range(rows):
            for col_num in range(columns):
                inverted_grid_num = (grid_count - 1) - grid_num

                if version == 1:
                    # Base version, no modifications
                    index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 2:
                    # For switching sets' sides
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 3:
                    # Inverting the vertical order of images within each set
                    index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                
                elif version == 4:
                    # Inverting the horizontal order of images within each set
                    index = grid_num * image_count + row_num * columns + (columns - 1 - col_num)
                
                elif version == 5:
                    # Invert the order of rows only in the left grid
                    if grid_num == 0:
                        index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 6:
                    # Only vertically flip the second grid
                    if grid_num == 1:  # Assuming the second grid is indexed as 1
                        index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 7:
                    # Switch columns of only the first set
                    if grid_num == 0:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 8:
                    # Switch columns of only the first set
                    if grid_num == 1:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 15:
                    # Flip the bottom two rows of both grids
                    if row_num in [1, 2]:  # Adjust for a 3-row grid
                        new_row_num = 3 - row_num  # Invert row_num for the bottom two rows
                    else:
                        new_row_num = row_num
                    index = grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 16:
                    # Flip the bottom two rows of grid 1 only
                    if grid_num == 0 and row_num in [1, 2]:  # Adjust for a 3-row grid and check for grid 1
                        new_row_num = 3 - row_num  # Invert row_num for the bottom two rows
                    else:
                        new_row_num = row_num
                    index = grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 17:
                    # Flip the bottom two rows of grid 2 only
                    if grid_num == 1 and row_num in [1, 2]:  # Adjust for a 3-row grid and check for grid 2
                        new_row_num = 3 - row_num  # Invert row_num for the bottom two rows
                    else:
                        new_row_num = row_num
                    index = grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 21:
                    # Rearrange rows for both sets: Third row on top, second row on bottom
                    if row_num == 0:
                        new_row_num = 1  # First row moves to the middle
                    elif row_num == 1:
                        new_row_num = 2  # Second row moves to the bottom
                    else:
                        new_row_num = 0  # Third row moves to the top
                    index = grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 22:
                    # Rearrange rows for set 1 only
                    if grid_num == 0:  # Applying the condition only to set 1
                        if row_num == 0:
                            new_row_num = 1  # First row moves to the middle
                        elif row_num == 1:
                            new_row_num = 2  # Second row moves to the bottom
                        else:
                            new_row_num = 0  # Third row moves to the top
                    else:
                        new_row_num = row_num  # No change for set 2
                    index = grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 23:
                    # Rearrange rows for set 2 only
                    if grid_num == 1:  # Applying the condition only to set 2
                        if row_num == 0:
                            new_row_num = 1  # First row moves to the middle
                        elif row_num == 1:
                            new_row_num = 2  # Second row moves to the bottom
                        else:
                            new_row_num = 0  # Third row moves to the top
                    else:
                        new_row_num = row_num  # No change for set 1
                    index = grid_num * image_count + new_row_num * columns + col_num
               
                elif version == 27:
                    # Flip columns and rows for both grids
                    modified_col_num = (columns - 1) - col_num  # Flipping columns horizontally
                    modified_row_num = (rows - 1) - row_num  # Flipping rows vertically
                    index = grid_num * image_count + modified_row_num * columns + modified_col_num
               
                elif version == 28:
                    # Flip columns for both grids and rows for grid 1 only
                    modified_col_num = (columns - 1) - col_num  # Flipping columns horizontally
                    if grid_num == 0:  # Grid 1
                        modified_row_num = (rows - 1) - row_num  # Flipping rows vertically
                    else:  # No row flip for Grid 2
                        modified_row_num = row_num
                    index = grid_num * image_count + modified_row_num * columns + modified_col_num
               
                elif version == 29:
                    # Flip columns for both grids and rows for grid 2 only
                    modified_col_num = (columns - 1) - col_num  # Flipping columns horizontally
                    if grid_num == 1:  # Grid 2
                        modified_row_num = (rows - 1) - row_num  # Flipping rows vertically
                    else:  # No row flip for Grid 1
                        modified_row_num = row_num
                    index = grid_num * image_count + modified_row_num * columns + modified_col_num

                elif version == 33:
                    # Flip rows vertically for both grids
                    modified_row_num = (rows - 1) - row_num
                    # Flip columns horizontally only in grid 1
                    if grid_num == 0:  # Grid 1
                        modified_col_num = (columns - 1) - col_num
                    else:  # Keep columns as is for Grid 2
                        modified_col_num = col_num
                    index = grid_num * image_count + modified_row_num * columns + modified_col_num
                            
                elif version == 34:
                    # Flip rows vertically for both grids
                    modified_row_num = (rows - 1) - row_num
                    # Flip columns horizontally only in grid 1
                    if grid_num == 1:  # Grid 1
                        modified_col_num = (columns - 1) - col_num
                    else:  # Keep columns as is for Grid 2
                        modified_col_num = col_num
                    index = grid_num * image_count + modified_row_num * columns + modified_col_num
                                
                
                
                
                
                
                
           # all same modifications but on the switched sets.      
                elif version == 9:
                   # inverted_grid_num = (grid_count - 1) - grid_num
                    # Inverting the vertical order of images within each set
                    index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                
                elif version == 10:
                   # inverted_grid_num = (grid_count - 1) - grid_num
                    # Inverting the horizontal order of images within each set
                    index = inverted_grid_num * image_count + row_num * columns + (columns - 1 - col_num)
                
                elif version == 11:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Invert the order of rows only in the left grid
                    if grid_num == 0:
                        index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 12:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Only vertically flip the second grid
                    if grid_num == 1:  # Assuming the second grid is indexed as 1
                        index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 13:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Switch columns of only the first set
                    if inverted_grid_num == 0:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = inverted_grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 14:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Switch columns of only the first set
                    if inverted_grid_num == 1:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = inverted_grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = inverted_grid_num * image_count + row_num * columns + col_num
               
                elif version == 18:
                    # Flip the bottom two rows of both grids
                    if row_num in [1, 2]:  # Adjust for a 3-row grid
                        new_row_num = 3 - row_num  # Invert row_num for the bottom two rows
                    else:
                        new_row_num = row_num
                    index = inverted_grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 19:
                    # Flip the bottom two rows of grid 1 only
                    if grid_num == 0 and row_num in [1, 2]:  # Adjust for a 3-row grid and check for grid 1
                        new_row_num = 3 - row_num  # Invert row_num for the bottom two rows
                    else:
                        new_row_num = row_num
                    index = inverted_grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 20:
                    # Flip the bottom two rows of grid 2 only
                    if grid_num == 1 and row_num in [1, 2]:  # Adjust for a 3-row grid and check for grid 2
                        new_row_num = 3 - row_num  # Invert row_num for the bottom two rows
                    else:
                        new_row_num = row_num
                    index = inverted_grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 24:
                    # Rearrange rows for both sets: Third row on top, second row on bottom
                    if row_num == 0:
                        new_row_num = 1  # First row moves to the middle
                    elif row_num == 1:
                        new_row_num = 2  # Second row moves to the bottom
                    else:
                        new_row_num = 0  # Third row moves to the top
                    index = inverted_grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 25:
                    # Rearrange rows for set 1 only
                    if grid_num == 0:  # Applying the condition only to set 1
                        if row_num == 0:
                            new_row_num = 1  # First row moves to the middle
                        elif row_num == 1:
                            new_row_num = 2  # Second row moves to the bottom
                        else:
                            new_row_num = 0  # Third row moves to the top
                    else:
                        new_row_num = row_num  # No change for set 2
                    index = inverted_grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 26:
                    # Rearrange rows for set 2 only
                    if grid_num == 1:  # Applying the condition only to set 2
                        if row_num == 0:
                            new_row_num = 1  # First row moves to the middle
                        elif row_num == 1:
                            new_row_num = 2  # Second row moves to the bottom
                        else:
                            new_row_num = 0  # Third row moves to the top
                    else:
                        new_row_num = row_num  # No change for set 1
                    index = inverted_grid_num * image_count + new_row_num * columns + col_num
                
                elif version == 30:
                    # Flip columns and rows for both grids
                    modified_col_num = (columns - 1) - col_num  # Flipping columns horizontally
                    modified_row_num = (rows - 1) - row_num  # Flipping rows vertically
                    index = inverted_grid_num * image_count + modified_row_num * columns + modified_col_num
               
                elif version == 31:
                    # Flip columns for both grids and rows for grid 1 only
                    modified_col_num = (columns - 1) - col_num  # Flipping columns horizontally
                    if grid_num == 0:  # Grid 1
                        modified_row_num = (rows - 1) - row_num  # Flipping rows vertically
                    else:  # No row flip for Grid 2
                        modified_row_num = row_num
                    index = inverted_grid_num * image_count + modified_row_num * columns + modified_col_num
               
                elif version == 32:
                    # Flip columns for both grids and rows for grid 2 only
                    modified_col_num = (columns - 1) - col_num  # Flipping columns horizontally
                    if grid_num == 1:  # Grid 2
                        modified_row_num = (rows - 1) - row_num  # Flipping rows vertically
                    else:  # No row flip for Grid 1
                        modified_row_num = row_num
                    index = inverted_grid_num * image_count + modified_row_num * columns + modified_col_num
                 
                elif version == 35:
                   # Flip rows vertically for both grids
                   modified_row_num = (rows - 1) - row_num
                   # Flip columns horizontally only in grid 1
                   if grid_num == 0:  # Grid 1
                       modified_col_num = (columns - 1) - col_num
                   else:  # Keep columns as is for Grid 2
                       modified_col_num = col_num
                   index = inverted_grid_num * image_count + modified_row_num * columns + modified_col_num     
                
                elif version == 36:
                   # Flip rows vertically for both grids
                   modified_row_num = (rows - 1) - row_num
                   # Flip columns horizontally only in grid 1
                   if grid_num == 1:  # Grid 1
                       modified_col_num = (columns - 1) - col_num
                   else:  # Keep columns as is for Grid 2
                       modified_col_num = col_num
                   index = inverted_grid_num * image_count + modified_row_num * columns + modified_col_num 
                
          # same as versions 1-14 but using vertically flipped images      
                elif version == 37:
                    # Base version, no modifications
                    index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 38:
                    # For switching sets' sides
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 39:
                    # Inverting the vertical order of images within each set
                    index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                
                elif version == 40:
                    # Inverting the horizontal order of images within each set
                    index = grid_num * image_count + row_num * columns + (columns - 1 - col_num)
                
                elif version == 41:
                    # Invert the order of rows only in the left grid
                    if grid_num == 0:
                        index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 42:
                    # Only vertically flip the second grid
                    if grid_num == 1:  # Assuming the second grid is indexed as 1
                        index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 43:
                    # Switch columns of only the first set
                    if grid_num == 0:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 44:
                    # Switch columns of only the first set
                    if grid_num == 1:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = grid_num * image_count + row_num * columns + col_num
                        
                elif version == 45:
                   # inverted_grid_num = (grid_count - 1) - grid_num
                    # Inverting the vertical order of images within each set
                    index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                
                elif version == 46:
                   # inverted_grid_num = (grid_count - 1) - grid_num
                    # Inverting the horizontal order of images within each set
                    index = inverted_grid_num * image_count + row_num * columns + (columns - 1 - col_num)
                
                elif version == 47:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Invert the order of rows only in the left grid
                    if grid_num == 0:
                        index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 48:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Only vertically flip the second grid
                    if grid_num == 1:  # Assuming the second grid is indexed as 1
                        index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 49:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Switch columns of only the first set
                    if inverted_grid_num == 0:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = inverted_grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 50:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Switch columns of only the first set
                    if inverted_grid_num == 1:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = inverted_grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                        
            # same as 1-14 but horizontally flipped individual images
                elif version == 51:
                    # Base version, no modifications
                    index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 52:
                    # For switching sets' sides
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 53:
                    # Inverting the vertical order of images within each set
                    index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                
                elif version == 54:
                    # Inverting the horizontal order of images within each set
                    index = grid_num * image_count + row_num * columns + (columns - 1 - col_num)
                
                elif version == 55:
                    # Invert the order of rows only in the left grid
                    if grid_num == 0:
                        index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 56:
                    # Only vertically flip the second grid
                    if grid_num == 1:  # Assuming the second grid is indexed as 1
                        index = grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 57:
                    # Switch columns of only the first set
                    if grid_num == 0:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = grid_num * image_count + row_num * columns + col_num
                
                elif version == 58:
                    # Switch columns of only the first set
                    if grid_num == 1:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = grid_num * image_count + row_num * columns + col_num
                        
                elif version == 59:
                   # inverted_grid_num = (grid_count - 1) - grid_num
                    # Inverting the vertical order of images within each set
                    index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                
                elif version == 60:
                   # inverted_grid_num = (grid_count - 1) - grid_num
                    # Inverting the horizontal order of images within each set
                    index = inverted_grid_num * image_count + row_num * columns + (columns - 1 - col_num)
                
                elif version == 61:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Invert the order of rows only in the left grid
                    if grid_num == 0:
                        index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 62:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Only vertically flip the second grid
                    if grid_num == 1:  # Assuming the second grid is indexed as 1
                        index = inverted_grid_num * image_count + (rows - 1 - row_num) * columns + col_num
                    else:
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 63:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Switch columns of only the first set
                    if inverted_grid_num == 0:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = inverted_grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                elif version == 64:
                    #inverted_grid_num = (grid_count - 1) - grid_num
                    # Switch columns of only the first set
                    if inverted_grid_num == 1:
                        # Calculate the modified column index for switching
                        modified_col_num = (columns - 1) - col_num
                        index = inverted_grid_num * image_count + row_num * columns + modified_col_num
                    else:
                        # No modification for other sets
                        index = inverted_grid_num * image_count + row_num * columns + col_num
                
                
                
                if version in range(37, 51):  # Assuming version 37 and 38 require flipped images
                   image_to_paste = images[index].transpose(Image.FLIP_TOP_BOTTOM)
                elif version in range(51, 65):
                    image_to_paste = images[index].transpose(Image.FLIP_LEFT_RIGHT)
                else:
                   image_to_paste = images[index]
                
                # Calculate `left` and `upper` for all versions
                left = grid_num * (columns * img_width + (columns - 1) * border_size + grid_spacing) + col_num * (img_width + border_size) + outer_border - grid_spacing // 2 + 25
                upper = row_num * (img_height + border_size) + outer_border

                # Adjust index based on the version if needed
                new_image.paste(image_to_paste, (left, upper))

    # Save the image for the current version
    new_image_path = f'C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\Variations\\BP_2_{version}.png'
    new_image.save(new_image_path)
    print(f"Saved: {new_image_path}")













# Loop through the versions and create/save each one
for i in range(1, 65):
    create_and_save_image(i)
