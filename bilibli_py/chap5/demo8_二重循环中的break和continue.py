# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 44
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j,end='\t')
    print()

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()