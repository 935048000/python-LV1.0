#!/usr/bin/env python
# coding=utf-8


'''
读写文本数据
读写各种不同编码的文本数据，比如 ASCII，UTF-8 或 UTF-16 编码等
"r"   以读方式打开，只能读文件 ， 如果文件不存在，会发生异常      
"w" 以写方式打开，只能写文件， 如果文件不存在，创建该文件,如果文件已存在，先清空，再打开文件
"rb"   以二进制读方式打开，只能读文件 ， 如果文件不存在，会发生异常      
"wb" 以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件,如果文件已存在，先清空，再打开文件
"rt"   以文本读方式打开，只能读文件 ， 如果文件不存在，会发生异常      
"wt" 以文本写方式打开，只能写文件， 如果文件不存在，创建该文件,如果文件已存在，先清空，再打开文件
"rb+"   以二进制读方式打开，可以读、写文件 ， 如果文件不存在，会发生异常      
"wb+" 以二进制写方式打开，可以读、写文件， 如果文件不存在，创建该文件,如果文件已存在，先清空，再打开文件
'''

with open('testfile.txt', 'rt') as f:
    data = f.read()
    print data
f.close()

with open('testfile.txt', 'rt') as f:
    for line in f:
        print line
f.close()

with open('testfile.txt', 'aw+') as f:
    f.write('hello')
    f.write('\n')
f.close()


# with open('testfile.txt', 'at') as f:
#     print(line1, file=f)
#     print(line2, file=f)
# f.close()




















