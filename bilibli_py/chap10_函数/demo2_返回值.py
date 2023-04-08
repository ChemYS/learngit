# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 89 返回值return
def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

a=[10,11,23,22,33,54,65]
print(fun(a))

#######################
def fun1():
    print('hello')
print(fun1())
fun1()

def fun2():
    return 'hello'
print(fun2())