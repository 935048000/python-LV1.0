if __name__ == '__main__':
    a = [1, 2, 3]
    
    b = a
    c = a[:]
    
    b[0] = 4
    print (b)
    print (a)
    
    c[0] = 5
    print (c)
    print (a)