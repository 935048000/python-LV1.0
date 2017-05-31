#!/usr/bin/env python
# coding=utf-8

'''
 合并拼接字符串
将几个小的字符串合并为一个大的字符串
 join() 方法
'''

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

print ' '.join(parts)
print ','.join(parts)
print ''.join(parts)
print


a = 'Is Chicago'
b = 'Not Chicago?'
print a + ' ' + b
print

print('{} {}'.format(a, b))
print(a + ' ' + b)
print

a = 'Hello' 'World'
print a

s = ''
for p in parts:
    s += p
data = ['ACME', 50, 91.1]
print ','.join(str(d) for d in data)

# print(a + ':' + b + ':' + c)
# print(':'.join([a, b, c]))
# print(a, b, c, sep = ':')

print f.write(chunk1 + chunk2)
print f.write(chunk1)
print f.write(chunk2)


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ''.join(sample())

for part in sample():
    f.write(part)

def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)

with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)