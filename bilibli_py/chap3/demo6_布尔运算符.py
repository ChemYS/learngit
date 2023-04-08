# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 24 布尔运算符
# and 当两个结果都为True，才是True
a,b=1,2
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)

# or 只要有一个结果True，就是True
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b==2)
print(a!=1 or b!=2)

# not
print(not (a!=1 or b!=2))

# in & not in
s='helloworld'
print('w' in s)
print('k' not in s)
print('w' not in s)