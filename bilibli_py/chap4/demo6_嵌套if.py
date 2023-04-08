# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 32

s=input('你是会员吗？y/n')
m=float(input('请输入购物的金额：'))
if s=='y':
    if m>=200:
        print('付款金额为：',m*0.8)
    elif m >= 100:
        print('付款金额为：', m * 0.9)
    else:
        print('不打折')
else:
    if m>=200:
        print('付款金额为：',m*0.95)
    else:
        print('不打折')
    print('非会员')