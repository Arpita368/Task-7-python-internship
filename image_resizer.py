from PIL import Image
import os

def resize(im, new_width):
    width, height = im.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = im.resize((new_width, new_height))
    return resized_image

files = os.listdir(r'C:\Users\arpit\OneDrive\Desktop\22CM064\images')
extensions = ["png", "jpeg", "jpg", "iso", "gif"]

for file in files:
    extension = file.split(".")[-1].lower()
    if extension in extensions:
        im = Image.open(os.path.join(r'C:\Users\arpit\OneDrive\Desktop\22CM064\images', file))   
        resized_image = resize(im, 400)
        filename = file.split(".")[0]
        filepath = os.path.join(r'C:\Users\arpit\OneDrive\Desktop\22CM064\images', f"{filename}_resized.{extension}")
        resized_image.save(filepath)
        print(f"Resized and saved: {filepath}")
