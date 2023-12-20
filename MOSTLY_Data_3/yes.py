import os
import glob

# Specify the path to the main folder containing subdirectories with images
main_folder_path = '/Users/USER/Desktop/RESEARCH PAPERS/Datasets/MOSTLY_Data_3'

# Define a list of allowed image file extensions
allowed_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']

# Recursive function to count images in all subdirectories
def count_images_in_directory(directory):
    image_files = []
    for ext in allowed_extensions:
        image_files.extend(glob.glob(os.path.join(directory, f'*.{ext}')))
    for subdir in os.listdir(directory):
        subdir_path = os.path.join(directory, subdir)
        if os.path.isdir(subdir_path):
            image_files.extend(count_images_in_directory(subdir_path))
    return image_files

# Get a list of all image files in the main folder and its subdirectories
image_files = count_images_in_directory(main_folder_path)

# Count the number of images
num_images = len(image_files)

# Print the number of images
print(f'The main folder and its subdirectories contain {num_images} images.')

