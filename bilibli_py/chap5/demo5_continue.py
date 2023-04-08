# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 41 要求输出1-50之间所有5的倍数
for i in range(1,51):
    if i%5==0:
        print(i)
print('------------')
for i in range(1,51):
    if i%5!=0:
        continue
    print(i)