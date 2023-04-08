# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 86 函数的创建和调用
def calc(a,b):
    c=a+b
    return c
s=calc(10,20)
print(s)

# 87 函数调用的参数传递、位置实参、关键字实参
def calc(a,b): # 形式参数，形参，位置是在函数的定义处
    c=a+b
    return c
s=calc(10,20)  # 实际参数，实参，位置是在函数的调用处
print(s)
# 上面是位置实参，下面演示关键字实参
def calc(a,b):
    c=a+b
    return c
s=calc(a=120,b=10)
print(s)

#88 参数传递的内存分析