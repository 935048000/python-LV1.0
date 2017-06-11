#!/usr/bin/env python
# coding=utf-8


'''
 创建临时文件和文件夹
在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉。
tempfile 模块中有很多的函数可以完成这任务。
为了创建一个匿名的临时文件，可以使用 tempfile.TemporaryFile 
'''


from tempfile import TemporaryFile
with TemporaryFile('w+t',encoding='utf-8',errors='ignore') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')
    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()


from tempfile import TemporaryDirectory
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)
    # Use the directory























