# P172 实例代码10.3 统计三国演义
import jieba


excludes = {"不可", "却说", "二人", "将军", "荆州"}
txt = open("./三国演义.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
# words = jieba.lcut(txt)
print(words)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del (counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
