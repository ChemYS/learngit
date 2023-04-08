# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 114
class Animal:
    def eat(self):
        print('动物会吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

class Person(object):
    def eat(self):
        print('人吃五谷杂粮')

#定义一个函数
def fun(obj):
    obj.eat()

fun(Dog())
fun(Cat())
fun(Animal())
print('----鸭子类型----')
fun(Person())
