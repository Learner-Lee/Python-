def isNum():
    try:
        a = eval(input("请随机输入一个字符串:\n"))
        if type(a) == int or type(a) == float or type(a) == complex:
            print('True')
        else:
            print('False')
    except:
        print('False')
isNum()