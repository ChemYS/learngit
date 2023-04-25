# 利用from.....import....导入Image模块和ImageDraw模块
from PIL import Image, ImageDraw
# 导入face_recognition模块
import face_recognition

# TODO 调用face_recognition模块的load_image_file()方法,将/Users/girls.jpg路径下的图片文件加载到numpy数组中
# 赋值给变量image
image = face_recognition.load_image_file("/Users/girls.jpg")

# TODO 调用face_recognition模块的face_landmarks()方法,查找image中所有面部
# 赋值给面部特征位置列表face_landmarks_list
face_landmarks_list = face_recognition.face_landmarks(image)
# TODO print()函数格式化输出f"在这张照片中我找到了 {len(face_landmarks_list)} 张人脸"
print(f"在这张照片中我找到了 {len(face_landmarks_list)} 张人脸")

# TODO 调用Image模块的fromarray()方法将image转换回图片
# 赋值给变量pil_image
pil_image = Image.fromarray(image)
# TODO 调用ImageDraw模块的Draw()方法画出pil_image图像
# 赋值给变量picture
picture = ImageDraw.Draw(pil_image)

# 遍历图像中面部特征位置列表中每一个面部特征元素
for face_landmarks in face_landmarks_list:
    # 定义面部特征名称列表facial_features
    facial_features = [
        'chin',
        'left_eyebrow',
        'right_eyebrow',
        'nose_bridge',
        'nose_tip',
        'left_eye',
        'right_eye',
        'top_lip',
        'bottom_lip'
    ]
    
    # TODO 遍历面部特征名称列表中每一个面部特征
    for facial_feature in facial_features:
        # TODO 调用line()方法在picture图像中画出每个面部的特征！
        picture.line(face_landmarks[facial_feature], width=5)

# TODO 保存图像pil_image到指定路径/Users/girls_face.jpg
pil_image.save("/Users/girls_face.jpg")