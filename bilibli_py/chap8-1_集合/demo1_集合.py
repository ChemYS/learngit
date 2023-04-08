# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 70
# 集合中元素不允许重复
s={'python','hello',90,2,5,5,2,90}
print(type(s))
print(s)

s1=set(range(6))
print(s1,type(s1))
s2=set([1,2,2,3,4,5])
print(s2,type(s2))
s3=set((1,2,3,3,65,65))
print(s3,type(s3))
s4=set('python')
print(s4,type(s4))
s5=set({'python',2,2,3,3,55})
print(s5,type(s5))

s6={}
print(s6,type(s6))
s7=set()
print(type(s7))