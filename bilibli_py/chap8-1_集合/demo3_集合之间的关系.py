# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
#72
s1={10,20}
s2={20,30}
print(s1==s2)
print(s1!=s2)

'''一个集合是否是另一个集合的子集'''
s1={10,20}
s2={20,30}
s3={10,20,30}
print(s1.issubset(s3))
'''超集'''
print(s3.issuperset(s1))

'''两个集合是否含有交集'''
print(s2.isdisjoint(s3)) #有交集为False