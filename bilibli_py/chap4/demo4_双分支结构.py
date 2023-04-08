# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 30
money=1000
s=int(input('请输入取款金额'))
if s<=money:
    money=money-s
    print('取款成功，余额是',money)
else:
    print('余额不足')

num=int(input('请输入一个整数'))
if num%2==0:
    print('num是偶数')
else:
    print('num是奇数')