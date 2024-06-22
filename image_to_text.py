import pytesseract
from PIL import Image

# Load the image from the file
image_path = "/mnt/c/Users/byamb/projects/databricks/images/q1.png"
text_path = "/mnt/c/Users/byamb/projects/databricks/texts/q1.txt"
image = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image)


with open(text_path, 'w') as file:
    file.write(text)