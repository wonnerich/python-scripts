import os
import sys
from PIL import Image

def convert_images_to_webp(directory, quality=80):
    webp_directory = os.path.join(directory, 'webp')
    os.makedirs(webp_directory, exist_ok=True)
    
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(directory, filename)).convert("RGB")
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            img.save(os.path.join(webp_directory, webp_filename), 'WEBP', quality=quality)

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    convert_images_to_webp(directory)

