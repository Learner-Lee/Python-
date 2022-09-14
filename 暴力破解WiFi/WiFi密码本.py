import itertools as its

# 迭代器

words = "1234567890"
r = its.product(words, repeat=8)
# 保存在文件中     追加
dic = open("pass.txt", "a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))

dic.close()
