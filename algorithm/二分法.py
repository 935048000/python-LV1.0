"""二分法"""
def search2(a, m):
    low = 0
    high = len (a)
    while low <= high:
        mid = int((low + high) / 2)
        if a[mid] < m:
            low = mid + 1
        elif a[mid] > m:
            high = mid - 1
        else:
            while a[mid-1] == m:
                mid -= 1
                if a[mid] != m:
                    return mid + 1
            return mid

    return -1

    #  print(search2([3,4,5,8,8,8,8,10,13,14],8))
