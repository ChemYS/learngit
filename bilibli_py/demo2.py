# config=UTF-8
#转义字符
print('hello\nworld')# \ +转义功能的首字母  n-->newline的首字符表示换行
print('hello\tworld')
print('helloooo\tworld')# \t 制表符每4个字符为一个，这里8个字符刚好占满2个制表符，所以新开一个比上面的长
print('hello\rworld')#world将hello进行了覆盖
print('hello\bworld')#\b是退格

print('http://www.baidu.com')
print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，R或r
print(r'hello\nworld')
#注意事项，最后一个字符不能是反斜杠
#print(r'hello\nworld\')
print(r'hello\nworld\\')