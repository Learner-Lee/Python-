txt = open("./三国演义.txt", "r", encoding='utf-8').read()
b = []
for i in txt:
    b.append(i)

a = 0
for index in range(len(b)):
    if b[index] == "曹":
        if b[index+1] == '操':
            a += 1
print(a)
