# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
#73
s1={10,20}
s2={20,30,40}
s3={10,20,30}
print(s1.intersection(s3))
print(s3 & s1) #交集

# 并集
print(s1.union(s2))
print(s1 | s2)

#差集
print(s1.difference(s2))
print(s1-s2)

# 对称差集
print(s1.symmetric_difference(s2))
print(s1^s2)