# coding:UTF-8
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=17&spm_id_from=pageDriver

# 61
scores={'张三':100,'李四':98,'王五':88}
print('张三' in scores)
print('张三' not in scores)

del scores['张三']
print(scores)
scores.clear()
print(scores)
scores['陈六']=98
print(scores)
scores['陈六']=100
print(scores)
# 62

k=scores.keys()
print(k)
print(type(k))
print(list(k))
v=scores.values()
print(v)
print(type(v))
i=scores.items()
print(i)
print(type(i))