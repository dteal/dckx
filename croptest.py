from PIL import Image

img = Image.open("lamp.png")

img2 = img.crop((0, 0, 100, 100))
img2.save("img2.png")
