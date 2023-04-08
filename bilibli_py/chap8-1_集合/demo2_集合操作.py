# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 71
s={10,20,30,40,50}
print(10 in s)
print(100 in s )
print(10 not in s)
print(100 not in s )

s.add(80)
print(s)
s.update({100,200,300})
print(s)
s.update([1,2,3])
s.update((7,8,9))
print(s)

s.remove(100)
print(s)
#s.remove(500)

s.discard(200) #不存在不报错
print(s)
s.discard(500)
print(s)

s.pop() #删除任意
print(s)
#s.pop(30) #删除任意
print(s)

s.clear()
print(s)