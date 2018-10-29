def div(a, b):
    try:
        print (a / b)
    except ZeroDivisionError:
        print ('Error:b 不能等于0')
    except Exception as e:
        e.args += ('more test...........',)
        print ('意想不到的错误', e)
        
        # raise
    else:
        print ('一切顺利')
    finally:
        print ('总是执行')
    return 0


if __name__ == '__main__':
    div (2, 0)
    print ()
    div (2, 'bad type')
    # print()
    # div(1,2)
