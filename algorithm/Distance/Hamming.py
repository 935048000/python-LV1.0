"""
海明距离
"""


def hamming_distance(s1, s2):
    assert len (s1) == len (s2)
    return sum (ch1 != ch2 for ch1, ch2 in zip (s1, s2))


print (hamming_distance ("gdads", "glass"))
