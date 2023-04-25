from PIL import Image
from face_recognition import *
import os
import random

image = load_image_file("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/girls.png")

face_locations = face_locations(image)

n = 1
for face_location in face_locations:
    print(face_location)
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f"C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/file/{n}.png")
    n += 1

image_names = os.listdir("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/file/")
lucky = random.choice(image_names)

lucky_dir = os.path.join("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/file/",lucky)
img_back = Image.open("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/back.png").resize((2000,2000))
verse =Image.open(lucky_dir)

def mix(img1,img2,coordinator):
    img1 = img1.resize((2000,2000))
    img2 = img2.resize((1000,1200))
    img1.paste(img2,coordinator)
    return img1

co = (500,350)
background = mix(img_back,verse,co)
background.save("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/success.png")
