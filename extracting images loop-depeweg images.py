from PIL import Image
import os
import re

# Base path where the images are located
base_path = 'C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\Depeweg images'

# Dimensions and positions for the squares
square_size = (214, 214)
column_starts = [6, 245, 656, 897]  # Starts for columns 1 and 2 of sets 1 and 2 respectively
row_starts = [5, 245, 485]  # Starts for rows 1, 2, and 3
border_size = 2  # Size of the border around each square

columns = 2
rows = 3
sets = 2

# Pattern to match files of interest (e.g., 'p001.png' to 'p099.png')
pattern = re.compile(r'p00\d{2}\.png')

# Get all files in the directory
files = os.listdir(base_path)

# Filter files based on the pattern
filtered_files = [f for f in files if pattern.match(f)]

# Loop through the filtered list of image files
for image_name in filtered_files:
    # Construct the full path of the image
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
                # Adjusted filename generation to use original image name for consistency
                filename = f'{image_name[:-4]}_{set_id}_{col_num}_{row_num}.png'
                save_path = os.path.join(base_path, filename)
                bordered_image.save(save_path)
