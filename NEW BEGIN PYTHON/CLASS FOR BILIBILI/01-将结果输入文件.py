# 将结果输入到文件中
pf = open('../CLASS 05/demotext01.txt', 'w')
print('i like python',file=pf)
pf.close()


"""
open(file, mode)

mode
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist
"""

'''
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
参数
objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
sep -- 用来间隔多个对象，默认值是一个空格。
end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
file -- 要写入的文件对象。
flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。
'''