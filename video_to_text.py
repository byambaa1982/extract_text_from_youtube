import cv2
import pytesseract
import os
import re
import hashlib

# Define the video file name
video_file = 'test60.mp4'

# Create a VideoCapture object
cap = cv2.VideoCapture(video_file)

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Create a directory to save the extracted text files if it doesn't exist
if not os.path.exists('extracted_text'):
    os.makedirs('extracted_text')

frame_count = 0
skip_factor = 500  # Process every 1500th frame
pattern = re.compile(r'\d{2} #')  # Pattern to match text containing a number followed by #

# Set to store hashes of the texts that have been saved
saved_texts = set()

def hash_text(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def normalize_text(text):
    # Find the pattern and remove everything before it
    match = pattern.search(text)
    if match:
        text = text[match.start():]
    text = text.strip()
    return text

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret:
        # Increment frame count
        frame_count += 1
        
        # Skip frames based on the skip_factor
        if frame_count % skip_factor != 0:
            continue
        
        # Use pytesseract to do OCR on the frame
        text = pytesseract.image_to_string(frame)
        
        # Check if the extracted text is more than 300 characters and matches the pattern
        if len(text) > 300 and pattern.search(text):
            # Normalize the text
            normalized_text = normalize_text(text)
            
            # Hash the normalized text and check if it has been saved before
            text_hash = hash_text(normalized_text)
            if text_hash not in saved_texts:
                # Add the text hash to the set
                saved_texts.add(text_hash)
                
                # Create a text file for the current frame
                text_filename = f'extracted_text/frame_{frame_count}.txt'
                with open(text_filename, 'w') as text_file:
                    # Write the frame number and the extracted text to the file
                    text_file.write(f"\n{normalized_text}\n")
    else:
        break

# Release the video capture object
cap.release()

print("Text extraction completed and saved to the 'extracted_text' directory.")
