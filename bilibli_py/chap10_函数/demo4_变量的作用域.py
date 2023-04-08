# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 93
def fun(a,b):
    c=a+b   # c称为局部变量，ab为函数的形参也是局部
    print(c)

name='test' # 全局变量
print(name)
def fun2():
    print(name)
fun2()

def fun3():
    global age  #声明为全局变量
    age=20
    print(age)
fun3()
print(age)