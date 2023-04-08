# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 52
# append 末尾添加一个
lst=[10,20,30]
print(lst,id(lst))
lst.append(100)
print(lst,id(lst))
# extend 末尾至少添加一个
lst2=['hh','ee']
#lst.append(lst2)
#print(lst,id(lst))
lst.extend(lst2)
print(lst,id(lst))
# insert 任意位置添加一个
lst.insert(1,90)
print(lst,id(lst))
# 任意位置添加多个，切片
lst3=[True,False,'test']
lst[1:]=lst3
print(lst,id(lst))

print('-------------------')
#53
# remove 有重复只移除第一个，一次删除一个
lst53=[10,20,30,30,40,50,60,60,30]
lst53.remove(30)
print(lst53)
# pop 删除一个指定索引位置上的元素，不指定会删除最后一个元素
lst53.pop(1)
print(lst53)
# lst53.pop(10) #error
lst53.pop()
print(lst53)
# 切片 删除至少一个元素，将产生一个新的列表对象
lst533=lst53[1:3]
print(lst53)
print(lst533)
# clear 清空列表
lst53.clear()
print(lst53)
# del 删除列表
del lst53
#print(lst53)

print('-------------------')
# 54
#
lst54=[10,20,30,40]
lst54[2]=100
print(lst54)
lst54[1:3]=100,200,400,300
print(lst54)
print('-------------------')
# 55
#
lst55=[20,90,10,50,99,81]
print(lst55,id(lst55))
lst55.sort()
print(lst55,id(lst55))
lst55.sort(reverse=True)
print(lst55,id(lst55))

print('使用内置函数sorted')
lst55=[20,90,10,50,99,81]
print(lst55,id(lst55))
lst55=sorted(lst55)
print(lst55,id(lst55))
lst55=sorted(lst55,reverse=True)
print(lst55,id(lst55))