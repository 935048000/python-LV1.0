
#输入1
N = int(input())

# 输入2
n = input()
n = n.strip(" ").split(" ")
if int(N) != len(n):
    exit(1)

# 计算绝对值差的次数
I = 0
for i in range(int(N)):
    I += i
#
# 绝对值差的容器
A =[]
# 输入2的长度
ns = len(n)
#
#
for nn in range(ns):
    n[nn] = int(n[nn])
#
#
# # 计算
# for j in range(ns-1):
#     s = n[j] - n[j+1]
#     A.append(abs(s))
#     for y in range(1,ns-1):
#         s = n[y] - n[y + 1]
#         A.append (abs(s))
#         # for x in range(2,ns):
#         #     s = n[x] - n[x + 1]
#         #     A.append (s)
#
# print(A)
# # abs()求绝对值
#
#
#
#
#
#
#
#
#
def minimumAbsoluteDifference(n, arr):
    arr.sort()
    s = abs(arr[1] - arr[0])
    for i in range(1, n-1):
        if(abs(arr[i] - arr[i+1]) < s):
            s = abs(arr[i] - arr[i+1])
    return s

print(minimumAbsoluteDifference(N,n))