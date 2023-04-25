#将照片分为九宫格
# TODO 从PIL中导入Image模块
from PIL import Image
# TODO 读取Kelly的照片
image = Image.open("yequbiancheng/2_quweigongju/4748/example.png")
# TODO 获取照片的宽度、高度，分别赋值给width, height
width = image.size[0]
height = image.size[1]
# TODO 定义九宫格每张图片的宽度
item_width = int(width) /3
# 定义一个空列表figure，储存每一张小图的信息
figure = []
# 遍历3列
for col in range(3):
    # 遍历3行
    for row in range(3):
        # TODO 获取左上角坐标x1,y1    
        x1 = row * item_width
        y1 = col * item_width
        # TODO 获取右下角坐标x2,y2   
        x2 = (row+1) * item_width
        y2 = (col+1) * item_width
        # 将左上角、右下角的坐标储存在列表location中
        location = [x1,y1,x2,y2]
        # TODO 将每张照片的坐标存储在嵌套列表figure中
        figure.append(location)