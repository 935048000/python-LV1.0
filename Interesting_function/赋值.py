"""
解构赋值

"""

# 解构
list = [" hello"," world",100]
a,b,c = list
print(a,b,c)
print(type(c))


# 解构
num = [1,2,3,4]
a,*b,c = num
print(a,b,c)
print()

std = [["a",(1,2,3)],["b",(4,5,6)]]
print(std)

for name,(t1,t2,t3) in std:
    print(name,t1,t2,t3)

print()

std = {
    "name":"a",
    "age":19,
}
for v1,v2 in std.items():
    print(v1,":",v2)



