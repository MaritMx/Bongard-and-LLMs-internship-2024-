from PIL import Image, ImageChops
import os

# Parameters
columns = 2
rows = 3
image_count = columns * rows  # Total images per grid
grid_count = 2  # Number of grids
border_size = 10  # Border size between images
outer_border = 20  # Outer border size around the entire image
grid_spacing = 50  # Space between grids

def flip_image(image, flip_type):
    """Flip image based on the flip_type."""
    if flip_type == "vertical":
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    elif flip_type == "horizontal":
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return image

def create_and_save_image(version, flip_type="none"):
    # Load the extracted images
    extracted_image_paths = [
        os.path.join('C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\Cleaned images\\png format', f'p0{i}_{set_id}_{col_num}_{row_num}.png')
        for set_id in range(1, grid_count + 1)
        for row_num in range(1, rows + 1)
        for col_num in range(1, columns + 1)
     ]

    # Load images 
    images = [Image.open(img_path) for img_path in extracted_image_paths]
    img_width, img_height = images[0].size

    # Adjusted calculations for side-by-side grids with outer borders and increased space between grids
    total_width = (img_width * columns + border_size * (columns - 1)) * grid_count + grid_spacing + outer_border * 2
    total_height = img_height * rows + border_size * (rows - 1) + outer_border * 2
    new_image = Image.new('RGB', (total_width, total_height), 'black')
    
    for grid_num in range(grid_count):
        for row_num in range(rows):
            for col_num in range(columns):
                if version == 1:
                    index = grid_num * image_count + row_num * columns + col_num
                elif version == 2:
                    modified_col_num = (columns - 1) - col_num
                    modified_row_num = (rows - 1) - row_num
                    index = grid_num * image_count + modified_row_num * columns + modified_col_num
              
                left = grid_num * (columns * img_width + (columns - 1) * border_size + grid_spacing) + col_num * (img_width + border_size) + outer_border - grid_spacing // 2 + 25
                upper = row_num * (img_height + border_size) + outer_border
                 image_to_paste = flip_image(images[index], flip_type)
                new_image.paste(image_to_paste, (left, upper))
     # Save the image for the current version
    new_image_path = f'C:\\Users\\Marit\\Downloads\\Documenten UvA\\ResMas\\Internship\\Bongard problems\\Variations\\BP_{i}_{version}_{flip_type}_inv.png'
    new_image.save(new_image_path)
    print(f"Saved: {new_image_path}")
 versions_to_skip = range(15, 27)
 for i in range(1, 100):
    for j in range(1, 3):  
        if j in versions_to_skip:
            continue
        for flip_type in ["none", "vertical", "horizontal"]:
            create_and_save_image(j, flip_type)
