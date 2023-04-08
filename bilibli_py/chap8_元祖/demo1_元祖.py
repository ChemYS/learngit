# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 66
#可变序列
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))
#不可变序列，字符串，元祖
s='hello'
print(id(s))
s=s+'world'
print(id(s))

# 67元祖的创建
t=('python','hello',100)
print(type(t))

t1=tuple(('python','hello',100))
print(t1)
print(type(t1))

t2=('test',)
print(t2)
print(type(t2))

t3=()
t4=tuple()