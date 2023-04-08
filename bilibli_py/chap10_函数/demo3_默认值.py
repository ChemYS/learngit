# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 90 默认值参数
def fun(a,b=10):
    print(a,b)

fun(30,20)
fun(20)

# 91 可变的位置参数、
def fun(*args):
    print(args)
fun(10)
fun(10,30)
# 可变关键字形参
def fun(**args):
    print(args)
fun(a=10)
fun(a=10,b=30)

#def fun2(*args,*a) 只能一个可变位置参数
#def fun2(**args,**a) 只能一个可变关键字参数
def fun3(*args,**args1):
    pass
'''def fun4(**args,*args1):
    pass'''

# 92



def fun(a,b=  10):
    print('a=',a)
    print('b=',b)