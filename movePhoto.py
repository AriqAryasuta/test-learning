import os
import shutil

def copy_corresponding_images(json_dir, image_dir, output_dir, image_extension=".jpg"):
    """Copy images that have corresponding JSON files with the same filename."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(json_dir):
        if filename.endswith('.json'):
            # Get the base filename without extension
            base_filename = os.path.splitext(filename)[0]
            # Construct the corresponding image filename
            image_filename = base_filename + image_extension
            image_path = os.path.join(image_dir, image_filename)
            
            if os.path.exists(image_path):
                # Copy the image to the output directory
                shutil.copy2(image_path, output_dir)
                print(f"Copied: {image_filename}")
            else:
                print(f"Image not found: {image_filename}")

# Usage
json_directory = 'motorcycleDatasets/det_annot/val'
image_directory = 'datasets/imgs/val'
output_directory = 'motorcycleDatasets/imgs/val'

copy_corresponding_images(json_directory, image_directory, output_directory)