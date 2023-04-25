#将照片分为九宫格,保存
# 从PIL中导入Image模块
from PIL import Image
# 读取Kelly的照片
image = Image.open('yequbiancheng/2_quweigongju/4748/example.png')
# 获取照片的宽度、高度，分别赋值给width, height
width = image.size[0]
height = image.size[1]
# 定义九宫格每张图片的宽度
item_width = int(width / 3)
# 定义一个空列表figure，储存每一张小图的信息
figure = []
# 遍历3列
for col in range(3):
    # 遍历3行
    for row in range(3):
        # 获取左上角坐标x1,y1    
        x1 = col * item_width
        y1 = row * item_width
        # 获取右下角坐标x2,y2   
        x2 = (col + 1) * item_width
        y2 = (row + 1) * item_width
        # 将左上角、右下角的坐标储存在列表location中
        location = [y1,x1,y2,x2]
        # 将每张照片的坐标存储在嵌套列表figure中
        figure.append(location)
        
# TODO 计数，方便给图片命名
# 分割图片编号从左到右，从上到下排列依次为0-8
count = 0
# TODO 遍历figure，切割图片
for i in figure:
    # TODO 切割图片
    image_new = image.crop(i)
    # 设置切割后的路径path_new
    path_new = "yequbiancheng/2_quweigongju/4748/test_image_new/" + "image" + str(count) +'.png'
    # TODO 将切割后的图片保存至path_new
    image_new.save(path_new)
    # TODO 更新count
    count += 1