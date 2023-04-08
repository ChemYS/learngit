# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 38
for i in range(10):
    print(i)
for i in 'Python':
    print(i)
#如果在循环体中不需要使用到自定义变量，可将自定义变量写为_
for _ in 'Python':
    print('呵呵')

print('使用for循环，计算1到100之间的偶数和')
sum=0
for i in range(1,101):
    if i %2==0:
        sum+=i
print(sum)

#39 test 输出100-999之间的水仙花数 153=3*3*3+5*5*5+1*1*1
for i in range(100,1000):
    ge=i%10
    shi=i//10%10
    bai=i//100
    #print(ge,shi,bai)
    if ge**3+shi**3+bai**3==i:
        print(i)