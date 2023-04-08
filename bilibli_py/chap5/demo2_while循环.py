# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 36-37
b=1
while b<10:
    print(b)
    b+=1

#求1到4的和
b=0
sum=0
while b<5:
    sum+=b
    b+=1
    print(sum)

#计算1到100之间的偶数和
c=1
sum=0
while c<=100:
    if not bool(c%2): #c%2==0:
        sum+=c
    c+=1
print(sum)