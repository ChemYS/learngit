# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 110
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',20)
print('为stu2绑定性别属性')
stu2.gender='女'
print(stu2.name,stu2.age,stu2.gender)

stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的,称函数')
stu1.show=show #动态绑定方法
stu1.show()