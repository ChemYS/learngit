# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 68
t=(10,[20,30],40)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
print(id(100))
#由于[20,30]是列表，列表是可变序列，所以可添加元素，内存地址不变
t[1].append(100)
print(t[1],type(t[1]),id(t[1]))