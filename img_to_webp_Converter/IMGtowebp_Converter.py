from PIL import Image

im = Image.open("WonneMedia_ogImage.png").convert("RGB")

im.save("output.webp", "WEBP", quality=80)

