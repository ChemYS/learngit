# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 115 特殊属性
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age

x=C('Jack',20) #是C类型的一个实例对象
print(x.__dict__) #实例对象的属性字典
print(C.__dict__)
print('-------------------------')
print(x.__class__) #对象所属的类
print(C.__bases__) #C类的父类类型的元祖
print(C.__base__) #类的基类
print(C.__mro__)  #类的层次结构
print(A.__subclasses__()) #子类的列表
print('------------------------')
# 116 特殊方法
a=20
b=100
c=a+b #两个整数类型的对象的相加操作
d=a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')

s=stu1+stu2 #在类编写__add__特殊方法后才可使用相加
print(s)
s=stu1.__add__(stu2)
print(s)

lst=[11,22,33,44]
print(len(lst)) #len是内容函数len
print(lst.__len__())
print(len(stu1))

# 117
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象的id为:{0}'.format(id(obj)))
        return obj
    def __init__(self, name, age):
        print('__init__被调用了，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age

print('object这个类对象的id为：{0}'.format(id(object)))
print('Person这个类对象的id为：{0}'.format(id(Person)))

#创建Person的类的实例对象
p1=Person('张三',20)
print('p1这个Person类的实例对象的id为：{0}'.format(id(p1)))