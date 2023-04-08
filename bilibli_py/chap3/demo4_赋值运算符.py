# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 22
# 赋值运算符，从右到左
i=3+4
print(i)

a=b=c=20
print(a,id(a))
print(b,id(b))
print(c,id(c))

a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a,type(a))
a/=3
print(a,type(a))
a//=2
print(a,type(a))
a%=2
print(a,type(a))

a,b,c=20,30,40
print(a,b,c)

print('---交换两个变量---')
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)