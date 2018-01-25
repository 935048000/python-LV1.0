"""

迭代器模式


"""

# class MyIter(object):
#     def __init__(self, n):
#         self.index = 0
#         self.n = n
#
#     def __iter__(self):
#         return MyIter (self.n)
#
#     def next(self):
#         if self.index < self.n:
#             value = self.index**2
#             self.index += 1
#             return value
#         else:
#             raise StopIteration()

def MyGenerater(n):
    index = 0
    while index < n:
        yield index ** 2
        index += 1

if __name__=="__main__":
    # lst=["hello Alice","hello Bob","hello Eve"]
    # lst_iter=iter(lst)
    # print(lst_iter)
    # print (next(lst_iter))
    # print (next(lst_iter))
    # print (next (lst_iter))
    # print (next (lst_iter))
    # print (next (lst_iter))

    x_square = MyGenerater (10)
    for x in x_square:
        print (x)
        
        
    