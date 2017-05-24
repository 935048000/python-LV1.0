#!/usr/bin/env python
# coding=utf-8

'''
序列中出现次数最多的元素
找出一个序列中出现次数最多的元素
Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
'''


words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的 3 个单词
top_three = word_counts.most_common(3)
print(top_three)
print
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

#手动增加计数,一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。
print word_counts['not']
print word_counts['eyes']


morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1
print word_counts['eyes']

print  word_counts.update(morewords)
print

#跟数学运算操作相结合
a = Counter(words)
b = Counter(morewords)
print a
print b

c = a + b
print c

d = a - b
print d



