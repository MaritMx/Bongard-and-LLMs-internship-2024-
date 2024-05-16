# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:55:52 2024

@author: Marit
"""

import random
from PIL import Image
import os

random.seed(3)

image_dir = "C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\Cleaned images\\png format"
unused_images_path = "C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\MC_variations\\Stimuli\\test\\neither"

problem_sets = ["p002", "p003", "p009", "p008", "p023", "p007", "p048", "p034", "p036", "p010", "p039", "p025", "p006", "p035"] # excludes p021 because unclear which stimuli

# Define the rows from which to pick names
rows = [
    ["p022_2_2_3", "p023_2_2_3", "p021_2_2_2"],
    ["p095_2_2_3", "p096_1_2_2", "p089_1_1_2"],
    ["p07_1_2_1", "p07_1_1_2", "p07_2_2_2"],
    ["p012_1_2_1", "p06_2_2_2", "p07_2_1_1"],
    ["p024_2_2_2", "p01_1_1_1", "p025_2_2_3"],
    ["p012_1_2_1", "p02_1_2_1", "p011_1_2_3"],
    ["p024_1_1_3", "p022_1_1_1", "P021_1_2_3"],
    ["p097_2_2_3", "p02_1_1_2", "p03_2_2_3"],
    ["p056_1_1_1", "p057_1_2_1", "p059_2_1_1"],
    ["p09_2_2_1", "p012_2_1_2", "p013_1_2_1"],
    ["p07_1_2_3", "p014_2_2_3", "p052_1_1_2"],
    ["p058_1_1_1", "p060_1_2_1", "p059_2_1_1"],
    ["p011_2_2_3", "p012_1_2_1", "p014_1_2_1"],
    ["p034_2_1_3", "p097_1_2_1", "p074_1_1_2"]
]

def process_and_save_images(image_path, problem_set, idx, flip_type):
    with Image.open(image_path) as img:
        if flip_type == "vertical":
            flipped_image = img.transpose(Image.FLIP_TOP_BOTTOM)
        elif flip_type == "horizontal":
            flipped_image = img.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            flipped_image = img.copy()  # For 'none' case, just copy the image

        filename = f"stim_{problem_set}_{idx + 1}_3_{flip_type}.png"
        flipped_image.save(os.path.join(unused_images_path, filename))

# Function to randomly select one name from each row, 8 times
def random_selection(rows):
    results = []
    for row in rows:
        results.extend([random.choice(row) for _ in range(8)])
    return results

# Generate the random selections
selected_names = random_selection(rows)
# for name in selected_names:
#     for _ in range(3):
#         print(name)
    
# Process and save images
idx = 0
for name in selected_names:
    problem_set_index = idx // 8  # This determines which problem set to use based on the index
    if problem_set_index < len(problem_sets):  # Check to avoid index out of range if more than 8*len(problem_sets) names
        problem_set = problem_sets[problem_set_index]
        image_path = os.path.join(image_dir, f"{name}.png")
        for flip_type in ["vertical", "horizontal", "none"]:
            process_and_save_images(image_path, problem_set, idx % 8, flip_type)
    idx += 1

print("Images processed and saved.")