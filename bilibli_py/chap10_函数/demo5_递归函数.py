# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 94
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))