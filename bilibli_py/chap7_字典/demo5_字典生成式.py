# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 65
items=['张三','李四','王五']
scores=[70,80,90]
d={items:scores for items,scores in zip(items,scores) }
print(d)