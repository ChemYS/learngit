# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 16&17&18

name='张三'
age=20

print(type(name),type(age))
print('我叫'+name+',今年'+str(age)+'岁')

print('----将其他类型转换成str类型----')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('----将其他类型转换成int类型----')
s1='128'
s2='76.77'
s3='Hello'
f1=98.8
b1=True
print(type(s1),type(s2),type(s3),type(f1),type(b1))
print(int(s1))
#print(int(s2)) 将str转成int类型，字符串是小数
#print(int(s3)) 数字串必须是整数
print(int(f1))
print(int(b1))

print('----将其他类型转换成float类型----')
s1='128.98'
s2='76'
s3='Hello'
b1=True
i1=98
print(type(s1),type(s2),type(s3),type(b1),type(i1))
print(float(s1))
print(float(s2))
#print(float(s3)) 字符串的数据是非数字串
print(float(b1))
print(float(i1))