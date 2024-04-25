import os
from PIL import Image

def convert_images_to_webp(directory, quality=80):
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img = Image.open(os.path.join(directory, filename)).convert("RGB")
            webp_filename = os.path.splitext(filename)[0] + '.webp'
            img.save(os.path.join(directory, webp_filename), 'WEBP', quality=quality)

# Usage
convert_images_to_webp('/path/to/your/directory')

