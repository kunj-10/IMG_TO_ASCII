import os
import sys
from pathlib import Path
from PIL import Image

# Defining the ASCII characters according to intensity
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def img_to_ascii(img, imageName: str):
    """
    Function to convert an image into an ASCII art

    Parameters:
    image to be converted
    name of the txt file to be made
    """
    img_pixels = img.load()

    os.makedirs('output', exist_ok=True)    # Making the output directory

    output_file_path = os.path.join('output', f'{imageName}.txt')

    # Opening the text file
    with open(output_file_path, 'w') as file:
        for i in range(img.height):
            for j in range(img.width):
                pixel_value = img_pixels[j, i]
                
                if isinstance(pixel_value, tuple) and len(pixel_value) == 4:
                    # If the RGBA format is present
                    if pixel_value[3] == 0:
                        # If transparent pixel then add empty space
                        file.write(' ')
                    else:
                        file.write(ASCII_CHARS[pixel_value[0] // 25])
                else:
                    # Converting as per Grayscale
                    file.write(ASCII_CHARS[pixel_value // 25])
                
            file.write('\n')


def resize_image(img, new_width=150):
    """
    Function to resize an image to required width

    Parameters:
    image to be resized
    new_width(default = 150)
    """
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))
    
    return img

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Correct usage is: python img_to_ascii.py <path/to/img_1> <path/to/img_2> ... ")
    
    images = sys.argv[1:]

    # Processing each image
    for image in images:

        imageName = Path(image).stem    # Getting the name of the image for text file

        try:
            img = Image.open(image).convert('RGBA')
        except Exception as err:
            print("Error Opening image:", image)
            print(err)
            continue

        # Converting to ASCII art
        img_to_ascii(resize_image(img), imageName)
