# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver
# 95
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))

for i in range(1,7):
    print(fib(i))