import os
import re

def process_files(directory):
    # Define the pattern to match "2 digits followed by #"
    pattern = re.compile(r'^(\d{2}) #')

    # Dictionary to store the longest file content for each question number
    longest_files = {}

    # Loop through all text files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            print(filename)
            with open(filepath, 'r') as file:
                content = file.read()
                # Check if the content starts with the pattern
                match = pattern.match(content)
                if match:
                    question_num = match.group(1)
                    if question_num in longest_files:
                        # If there's already a file for this question number, check lengths
                        if len(content) > len(longest_files[question_num]):
                            longest_files[question_num] = content
                    else:
                        # If this is the first file for this question number, store it
                        longest_files[question_num] = content

    # Write the longest content for each question number to new files
    for question_num, content in longest_files.items():
        new_filename = f"question_{question_num}.txt"
        new_filepath = os.path.join(directory, new_filename)
        with open(new_filepath, 'w') as new_file:
            new_file.write(content)
        print(f"Created/Updated: {new_filename}")

# Specify the directory containing text files
directory = "/mnt/c/Users/byamb/projects/databricks/extracted_text/"

# Call the function to process the files
process_files(directory)
