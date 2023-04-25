# 制作图形照片墙
# 导入PIL模块
import PIL
# 从PIL模块中导入Image
from PIL import Image 

# 将文件夹路径赋值给变量path
path = r"C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/44"
# TODO 使用input()函数"输入图片名称(爱心/520/1314):"
# 赋值给变量pngName
pngName = input("输入图片名称(爱心/520/1314):")
# 将输入的图片名称构造正确的读取路径并赋值给fileName
fileName = path + "/" +pngName + ".png"

# TODO 使用open()函数打开fileName
# 赋值給变量img
img = Image.open(fileName)
# 使用convert()函数将图片转化为二值图片
# 赋值給变量img_1
img_1=img.convert("1") 
 # 把图像的size重新设定为(20,20)，也就是宽20像素，长20像素
 # 赋值給变量new_img
new_img = img_1.resize((20,20))
# 定义一个空列表figure
figure = []
# 使用for循环遍历0到19
for i in range(20):
    # 定义一个空列表row存储一行中每一列的值，0或1
    row = []
    # 使用for循环遍历0到19
    for j in range(20):
        # 使用getpixel()函数获取图像中某一点像素的RGB颜色值
        pix = new_img.getpixel((j,i))
         # 使用取模运算把颜色值255转化为1
        pix_new = pix % 254
        # 将转化后的值依次存储到列表row中
        row.append(pix_new)
    # 将每一行值存储在列表figure中      
    figure.append(row)
# 设置单张图片的像素，图片宽度pic_width为100像素，长度pic_height为100像素
pic_width = 100
pic_height = 100

# TODO 读取路径为"/Users/qian/pink.png"的背景图片
# 将背景图片的尺寸设置为(2000，2000)
img_back = Image.open(r"C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/44/pink.png").resize((2000,2000))
# 导入os模块
import os
# 读取路径为"/Users/qian/model"的照片
image_names = os.listdir(r"C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/44/model/")

# 获取嵌套列表的行数
row_num = len(figure)
# 获取嵌套列表的列数
column_num = len(figure[0])
# 导入random模块
import random

# 遍历行和列，判断当数值为0时
for row in range(row_num):
    for column in range(column_num):
        if figure[row][column] == 0:
            # TODO 随机选取文件夹"/Users/qian/model/"中的一张照片，把图片路径赋值給变量ran_photo
            ran_photo = "C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/44/model/" + random.choice(image_names)
            #print(ran_photo)
            # TODO 打开随机选中的照片，并且将照片的尺寸设置宽度为pic_width，高度为pic_height
            pic = Image.open(ran_photo).resize((pic_width,pic_height))
            # TODO 使用paste()函数将选中的照片依次粘贴到照片背景img_back中
            # 参数设置为需要粘贴的图片pic，粘贴的位置图片宽度*列，图片高度*行
            img_back.paste(pic,(pic_width * column,pic_height* row))
# TODO 将图片保存到路径："/Users/qian/model.png"中
img_back.save(r"C:/Users/ChemYS/learngit/yequbiancheng/2_quweigongju/44/model.png")