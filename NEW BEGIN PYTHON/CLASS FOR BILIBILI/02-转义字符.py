# 转义字符
print('hello\nworld')   # \+转移功能的首字母    n----》newline的首字母表示换行
print('hell\tworld')   # t----》tab的首字母表示缩进
print('hello\tworld')
print('hello00\tworld')
print('hell\rworld')    # world将hello进行覆盖
print('hell\bworld')    # \b是退一个格，将o退没了 b----》backspace的首字母表示退格

print('http:\\\\www.google.com')
print('老师说：\'大家好\'')


# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r,或R
print(r'hell\rworld')
# 注意事项，最后一个字符不能是反斜杠
# print(r'hell\rworld\')
print(r'hell\rworld\\')

