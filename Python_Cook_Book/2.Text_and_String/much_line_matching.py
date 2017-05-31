#!/usr/bin/env python
# coding=utf-8

'''
多行匹配模式
使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配。

'''
import re

comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */
'''

print comment.findall(text1)
print comment.findall(text2)

# (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print comment.findall(text2)
print

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print comment.findall(text2)






