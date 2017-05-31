#!/usr/bin/env python
# coding=utf-8

'''
审查清理文本字符串
选择使用字符串函数 (比如 str.upper() 和 str.lower() ) 将文本转为标准格式。
使用 str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定的字符序列。

'''
import unicodedata
import sys

s = 'pýtĥöñ\fis\tawesome\r\n'
print s

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None
}

a = s.translate(remap)
print a

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print b
print  b.translate(cmb_chrs)

digitmap = { c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd' }

print len(digitmap)

x = '\u0661\u0662\u0663'
print  x.translate(digitmap)
print a
b = unicodedata.normalize('NFD', a)
print b.encode('ascii', 'ignore').decode('ascii')


def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s