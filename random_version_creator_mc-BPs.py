# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:08:03 2024

@author: Marit
"""

import os
import random
from PIL import Image

random.seed(2)  # Fixed seed for reproducibility

# Parameters
columns = 2
rows = 2
grid_count = 2  # Number of grids
border_size = 10  # Border size between images
outer_border = 20  # Outer border size around the entire image
grid_spacing = 50  # Space between grids



# Paths
image_dir = "C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems"
base_save_path = "C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\MC_variations"

# Ensure output directory exists
os.makedirs(base_save_path, exist_ok=True)

# Load and classify images into two sets based on their prefix (p02_1 and p02_2)
image_sets = {1: [], 2: []}
for filename in os.listdir(image_dir):
    if filename.startswith('p02_1_'):
        image_sets[1].append(os.path.join(image_dir, filename))
    elif filename.startswith('p02_2_'):
        image_sets[2].append(os.path.join(image_dir, filename))

# Define the image manipulation function
def flip_image(image, flip_type):
    if flip_type == "vertical":
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    elif flip_type == "horizontal":
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return image

randomized_image_orders = {}

for attempt in range(25):  # Pre-determine 25 unique configurations
    # Shuffle and store image orders for each set
    randomized_image_orders[attempt] = {}
    for set_id in image_sets:
        shuffled_images = image_sets[set_id].copy()
        random.shuffle(shuffled_images)
        randomized_image_orders[attempt][set_id] = shuffled_images[:4]  # Take the first four images for each set

def generate_and_save_combined_images(flip_type="none"):
    for attempt, image_order in randomized_image_orders.items():
        # Create a new combined image for the two grids
        img_sample = Image.open(list(image_order[1])[0])  # Open the first image to get size
        img_width, img_height = img_sample.size
        total_width = 2 * (img_width * 2 + border_size) + grid_spacing + outer_border * 2
        total_height = img_height * 2 + border_size + outer_border * 2
        combined_image = Image.new('RGB', (total_width, total_height), 'white')

        for set_id, images in image_order.items():
            for i, img_path in enumerate(images):
                with Image.open(img_path) as img:
                    img = flip_image(img, flip_type)  # Apply flipping
                    row, col = divmod(i, 2)
                    x = outer_border + (set_id - 1) * (2 * img_width + border_size + grid_spacing) + col * (img_width + border_size)
                    y = outer_border + row * (img_height + border_size)
                    combined_image.paste(img, (x, y))

        # Save the combined image
        save_path = os.path.join(base_save_path, f'combined_set_version{attempt + 1}_{flip_type}.png')
        combined_image.save(save_path)
        print(f'Saved: {save_path}')

# Generate and save images for each mirroring type with the same order
for flip_type in ["none", "horizontal", "vertical"]:
    generate_and_save_combined_images(flip_type=flip_type)
