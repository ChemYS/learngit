# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 40
for i in range(3):
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

a=0
while a<3:
    pwd=input('请输入密码')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1