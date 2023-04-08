# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 110
# 封装 提高程序的安全性
# 继承 提高代码的复用性
# 多态 提高程序的可扩展性和可维护性
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)

stu1=Student('张三',20)
stu1.show()
print(stu1.name)
#print(stu.__age)
print(dir(stu1))
print(stu1._Student__age)

print('------------111----------')
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
#定义子类
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
stu=Student('Jack',20,'1001')
stu.info()
print('------------112----------')
#方法重写
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('姓名:{0},年龄:{1}'.format(self.name,self.age))
#定义子类
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score=score
    def info(self):
        super().info()
        print(self.score)
stu=Student('Jack',20,'1001')
stu.info()