# TODO 利用from.....import....导入turtle模块所有函数
from turtle import *

# TODO 定义一个绘制圆环的函数getCircle()，参数为color，设置画笔颜色为参数color，画笔粗细为5，圆半径为50
def getCircle(color):
    # 落下画笔
    pendown()
    pencolor(color)
    pensize(5)
    circle(50)
    # 抬起画笔
    penup()

# 隐藏画笔
hideturtle()
# TODO 抬起画笔
#penup()

# TODO 在（-80，0）（0，0）（80，0）（-40，-80）（40，-80）绘制五环
goto(-80,0)
getCircle("blue")
goto(0,0)
getCircle("black")
goto(80,0)
getCircle("red")
goto(-40,-80)
getCircle("yellow")
goto(40,-80)
getCircle("green")