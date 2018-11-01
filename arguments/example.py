import argparse
from argparse import ArgumentParser

if __name__ == '__main__':
    
    ap = ArgumentParser ()
    # ap.add_argument("-f", required = True, help = "文件名称")
    ap.add_argument ("-d", help="数据库")
    ap.add_argument ("-show", help="显示结果个数")
    args = vars (ap.parse_args ())
    print (args)
    print (args['d'])
    print (type (args['show']))
    arg2 = args['show']
    print (int (arg2[:4]),
           int (arg2[4:6]),
           int (arg2[6:8]),
           int (arg2[8:10]),
           int (arg2[10:12]),
           int (arg2[12:14]))
    
    if args['d']:
        print ('yes')
    else:
        print ('no')
