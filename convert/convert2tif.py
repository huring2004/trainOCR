from PIL import Image

for i in range(2001,2006):
    Image.open(f"../photo/image{i}.png").convert("L").save(f"image{i}.tif")