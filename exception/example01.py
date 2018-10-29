def div(a, b):
    try:
        print (a / b)
    except ZeroDivisionError:
        print ('Error:b 不能等于0')
    except Exception as e:
        # 对异常增加解释
        e.args += ('more test...........',)
    
        # 不中断执行，打印/输出 异常
        print ('意想不到的错误', e)
    
        # 中断执行，返回异常
        # raise
    else:
        print ('一切顺利')
    finally:
        print ('总是执行')

    print ('run right!')
    return 0


if __name__ == '__main__':
    div (2, 0)
    print ()
    div (2, 'bad type')
    # print()
    # div(1,2)
