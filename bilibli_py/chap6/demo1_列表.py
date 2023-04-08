# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 45 46 47
a=10 # 变量存储的是一个对象的引用
lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)

print('--------------------------')
'''
特点：
列表元素按顺序有序排序
索引映射唯一数据
可以存储重复数据
任意数据类型混存
根据需要动态分配和回收内存
'''
lst2=list(['hello','world',98])
print(lst2)
for i in lst2:
    print(i)
print(lst[0])
print(lst[-3])
print('--------------------------')
# 49
lst3=['hello','world',98,'hello','world',198]
print(lst3[2])
print(lst3[-3])
print('--------------------------')
# 50 获取列表的多个元素与切片
lst4=[10,20,30,40,50,60,70,80,90]
print(lst4[1:6:])# 新的列表
print(id(lst4))
lst5=lst4[1:6:1]
print(id(lst5))
lst5=lst4[:6:1]
print(lst5)
lst5=lst4[1::2]
print(lst5)
lst5=lst4[::-2]
print(lst5)
print('--------------------------')
# 51 列表元素的判断与遍历
lst51=[10,20,'python','hello']
print(10 in lst51)
print(100 in lst51)
print(10 not in lst51)
print(100 not in lst51)
for i in lst51:
    print(i)