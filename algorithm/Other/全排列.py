import time
import itertools
"""
全排列算法
"""
def print_time(arr):
    def _time_cha(list):
        t1 = time.time()
        ret = arr(list)
        print ((time.time() - t1),"s")
        print (ret)
        return ret
    return _time_cha


# 快
def test(l):
    # L = []
    # L = list(itertools.permutations (l, len(l)))
    # for i in range(len(L)):
    #     L[i] = list(L[i])
    # return L

    if len(l) <=1:
        yield l
    else:
        for perm in test(l[1:]):
            for i in range(len(l)):
                yield perm[:i] + l[0:1] + perm[i:]

# 慢
class Solution(object):
    def permute(self, list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        self._dfs(list,sub)
        return self.res

    def _dfs(self, Nums, subList):
        if len(subList) == len(Nums): # 当子空间的长度等于列表长度则把子空间加入到结果列表
            #print res,subList
            self.res.append(subList[:])
        for m in Nums:
            if m in subList: # 判断列表内的元素是否在子空间内
                continue     # 在的话跳出本次循环
            subList.append(m)# 不在就加入子空间
            self._dfs(Nums,subList)
            subList.remove(m)


s = Solution ()
# t1 = time.time ()
print (s.permute ([1, 2, 3]))
# print ((time.time () - t1), "s")



# t2 = time.time ()
# T = list(test([1,2,3]))
# print(T)
#print(str(T[0]).strip("[]").strip(","))
# print ((time.time () - t2), "s")