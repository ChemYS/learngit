# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#变量的赋值
cpu1=CPU()
cpu2=cpu1
print(cpu1)
print(cpu2)

#类的浅拷贝:对象包含的子对象内容不拷贝
print('-----------')
disk=Disk() #创建一个硬盘类的对象
computer1=Computer(cpu1,disk) #创建一个计算机类的对象
import copy
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)

#深拷贝：递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同
computer3=copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk)