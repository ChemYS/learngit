# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 109
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
    def sm():
        print('我使用了staticmethod修饰')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，我使用了classmethod修饰')

#类属性的使用方法
#print(Student.native_pace)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='天津'
print(stu1.native_pace)
print(stu2.native_pace)
print('-----------------')
#类方法的使用方式
Student.cm()
print('-----------------')
#静态方法的使用方式
Student.sm()