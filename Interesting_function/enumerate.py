


list = [2,4,6,8,10]

# 大众写法
for i in range(len(list)):
    print(i," is ",list[i])

# 高手写法
for i,val in enumerate(list):
    print(i," --> ",val)

