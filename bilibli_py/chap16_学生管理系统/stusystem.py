# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
#133

import os
import re
def main():
    while True:
        menu()
        choice=int(input('请选择序号执行功能'))#序号直接空格报错
        if choice in range(0,8):
            if choice==0:
                answer=input('您确定要退出系统吗y/n')
                if answer=='y' or answer=='Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()
        else:
            pass
def menu():
    print('================学生信息管理系统=============================')
    print('学生信息管理系统'.center(60,'='))
    print('功能菜单'.center(60,'='))
    print('1.录入学生信息'.center(60,' '))
    print('2.查找学生信息'.center(60, ' '))
    print('3.删除学生信息'.center(60, ' '))
    print('4.修改学生信息'.center(60, ' '))
    print('5.排序学生信息'.center(60, ' '))
    print('6.统计学生总人数'.center(60, ' '))
    print('7.显示所有学生信息'.center(60, ' '))
    print('0.退出'.center(60, ' '))
    print(''.center(60, '='))
def insert():
    student_list=[]
    while True
def search():
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == '__main__':
    main()