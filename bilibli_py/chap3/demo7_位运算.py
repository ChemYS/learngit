# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 25 位运算
# 按位与& 同为1时结果为1
print(4&8)
#00000100 4
#00001000 8
#00000000 4&8

# 按位或| 同为0时结果为0
print(4|8)
#00000100 4
#00001000 8
#00001100 4&8

# 左移位右移位
print(4<<1) #左移1位
print(4<<2) #左移2位

print(256<<1) #左移1位

print(4>>1) #右移1位
print(4>>2) #右移2位

print(4>>3) #右移3位
print(4>>4) #右移4位