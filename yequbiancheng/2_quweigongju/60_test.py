# 授人以鱼
# 利用from.....import....导入Image模块和ImageDraw模块
from PIL import Image
# 导入face_recognition模块
from face_recognition import *
# TODO 调用face_recognition模块的load_image_file()方法,将/Users/girls.jpg路径下的图片文件加载到numpy数组中
# 赋值给变量image
image = load_image_file("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/girls.png")

# TODO 调用face_recognition模块的face_landmarks()方法,查找image中所有面部
# 赋值给面部特征位置列表face_landmarks_list
face_locations = face_locations(image)
# TODO print()函数格式化输出f"在这张照片中我找到了 {len(face_landmarks_list)} 张人脸"
#print(f"在这张照片中我找到了 {len(face_landmarks_list)} 张人脸")
n = 1
# 利用for遍历face_locations中的每一个元组
for face_location in face_locations:
    # 将元组中的数据依次赋值给top, right, bottom, left
    print(face_location)
    top, right, bottom, left = face_location
    # 按照从上到下从左到右的位置顺序裁剪图片中的人脸数据并赋值给face_image
    face_image = image[top:bottom, left:right]
    # 使用fromarray方法将保存好的人脸数据转换为新的图片
    pil_image = Image.fromarray(face_image)
    # TODO 使用pil_image.save()方法将图片保存到路径f"/Users/Yoyo/{n}.png"中
    pil_image.save(f"C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/file/{n}.png")
    # TODO 记数变量加1
    n += 1
import os
import random
image_names = os.listdir("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/file/")
ran_photo = "C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/file/" + random.choice(image_names)

pic = Image.open(ran_photo).resize((1000,1000))
img_back = Image.open("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/back.png").resize((2000,2000))
img_back.paste(pic,(500,350))
img_back.save("C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/60/success.png")
