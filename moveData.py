import json
import os
import shutil

def has_traffic_sign(data):
    """Check if 'traffic sign' category exists in the JSON data."""
    if 'frames' in data:
        for frame in data['frames']:
            if 'objects' in frame:
                for obj in frame['objects']:
                    if obj.get('category') == 'motor':
                        return True
    return False

def process_json_files(source_dir, destination_dir):
    """Process JSON files and move those with 'traffic sign' category."""
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(source_dir, filename)
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                
                if has_traffic_sign(data):
                    shutil.copy2(file_path, destination_dir)
                    print(f"Copied: {filename}")
                else:
                    print(f"Skipped: {filename} (no motorcycle)")
            except json.JSONDecodeError:
                print(f"Error: Unable to parse {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Usage
source_directory = 'datasets/det_annot/val'
destination_directory = 'motorcycleDatasets/det_annot/val'

process_json_files(source_directory, destination_directory)