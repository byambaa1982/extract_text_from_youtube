import os
import glob

# Define the directory
directory = "/mnt/c/Users/byamb/projects/databricks/extracted_text/"

# Use glob to find all files that start with 'frame'
files_to_remove = glob.glob(os.path.join(directory, "frame*"))

# Iterate over the list of files and remove them
for file_path in files_to_remove:
    try:
        os.remove(file_path)
        print(f"Removed file: {file_path}")
    except Exception as e:
        print(f"Error removing file {file_path}: {e}")
