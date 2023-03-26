import thulac
thu1 = thulac.thulac(seg_only=True) #只进行分词，不进行词性标注
txt = open("./三国演义.txt", "r", encoding='utf-8').read()
words = thu1.cut("我爱你中国",text=False)
print(words)
count = []
a = 0
for word in words:
    if len(word[0]) == 1:
        continue
    else:
        if word[0] == '中国':
            a += 1
print(a)
