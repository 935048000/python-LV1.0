#!/usr/bin/env python
# coding=utf-8

'''
 在字符串中处理 html 和 xml
将 HTML 或者 XML 实体如 &entity; 或 &#code; 替换为对应的文本。再者，
你需要转换文本中特定的字符 (比如<, >, 或 &)。
替换文本字符串中的 ‘<’ 或者 ‘>’ ，使用 html.escape() 函数可以很容易
的完成。
'''

import html

s = 'Elements are written as "<tag>text</tag>".'

print(s)
print(html.escape(s))
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print s.encode('ascii', errors='xmlcharrefreplace')


s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print p.unescape(s)

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print unescape(t)



