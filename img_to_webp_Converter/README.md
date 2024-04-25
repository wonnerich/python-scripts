# Image to WebP Converter

This Python script converts images in a directory to the WebP format and saves them in a new directory named "webp" within the provided directory.

## Requirements

- Python 3
- Pillow library

## Usage

1. Install the required Python library: `pip install pillow`
2. Run the script with the directory as an argument: `python IMGtowebp_Converter.py [directory]`

If no directory is provided, the script will default to the current directory.

## How it works

The script scans the provided directory for image files with the extensions .png, .jpg, or .jpeg. For each image file, it opens the image, converts it to the RGB color space (if necessary), and then saves it in the WebP format in a new directory named "webp". The quality of the converted images can be adjusted by modifying the `quality` parameter in the `convert_images_to_webp` function.

## License

This project is licensed under the terms of the MIT license.