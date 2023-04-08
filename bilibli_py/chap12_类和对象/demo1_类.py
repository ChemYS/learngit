# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
#107
class Student: # 类名由一个或多个单词组成，每个单词的首字母大写，其余小写
    pass

# Python中一切皆对象
print(id(Student))
print(type(Student))
print(Student)

#类的组成 类属性 实例方法 静态方法 类方法
class Student: # 类名由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_pace="吉林" #直接写在类里面的变量，称为类属性
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #实例方法
    def eat(self):
        print('学生在吃饭')
    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod修饰')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，我使用了classmethod修饰')
#在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')

#创建Student类的对象
#实例对象
stu1=Student('张三',30)
print(id(stu1))
print(type(stu1))
print(stu1) # 输出id的十六进制的值
print('---------------------')
#类对象
print(id(Student))
print(type(Student))
print(Student)