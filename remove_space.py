import os

def remove_leading_whitespace(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
            with open(file_path, 'w') as file:
                for line in lines:
                    file.write(line.lstrip())

# Specify the directory containing text files
directory = "/mnt/c/Users/byamb/projects/databricks/extracted_text/"
remove_leading_whitespace(directory)
print("Leading whitespace removed from all text files in the directory.")
