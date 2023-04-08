# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 113
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '我的名字是{0}，今年{1}岁'.format(self.name,self.age)
stu=Student('张三',20)
print(dir(stu))
print(stu)
print(type(stu))