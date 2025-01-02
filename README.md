# IMG_TO_ASCII
This Python script converts images to ASCII art and saves the result in text files. It uses Pillow to load and manipulate images, and the output is saved as a text file with each pixel represented by ASCII characters based on their grayscale value.

## Features
- Converts images to ASCII art.
- Supports both RGBA (with transparency) and grayscale images.
- Resizes images to fit within the specified width while maintaining the aspect ratio.
- Saves ASCII art to text files in an output directory.

## Installation
1. Clone or download this repository to your local machine.

2. Install the required dependencies using pip:

``` bash
pip install -r requirements.txt
```
Alternatively, you can install Pillow the only required package manually:

``` bash
pip install Pillow
```

## Usage
- Place your image(s) in the same directory as the script or specify the full path to your image(s).

- Run the script from the terminal:

```bash
python img_to_ascii.py <path/to/image1> <path/to/image2> ...
```
*Replace <path/to/image1>, <path/to/image2>, etc., with the actual image paths.*


The script will resize the image(s) and convert them to ASCII art, saving the results as .txt files in the output folder. The filename of the generated text file will be the same as the original image's name.

### Example:

```bash
python img_to_ascii.py cat.png dog.jpg
```

This will create cat.txt and dog.txt inside the output folder.

## How It Works
- **Image Processing:** The script loads the image and converts it into a grayscale format (for RGBA images, transparency is handled).
- **Resize:** The image is resized to fit within a specified width (default 150px).
- **ASCII Mapping:** Each pixel is mapped to an ASCII character based on its intensity, with darker pixels represented by more complex characters (@, #, S, etc.) and lighter pixels by simpler characters (., ,).

## Customization
- You can adjust the width of the resized image by passing a different value for new_width in the resize_image() function (default is 150).
- You can modify the ASCII_CHARS list to change which characters are used to represent different pixel intensities.
