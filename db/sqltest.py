# coding=utf-8
import pymysql
from sys import argv
from os import path

def file2data(filename):
    """
    :param filename:
        data file name --> /path.../filename
    :return:
        data --> [[ticket,name_id,name,date],[],[],....]
            ticket:int
            name_id:int
            name:char
            date:char
    """
    with open (filename, "r", encoding="utf-8") as f:
        linedata = f.readlines ()
        lens = len (linedata)
        data = []
        for i in range (lens):
            line = linedata[i]
            line = line.strip ("\n").split (",")
            line[0] = int(line[0])
            line[1] = int(line[1])
            data.append (line)
    return data


def data2exesql(data):
    """
    :param data:
        data --> [[ticket,name_id,name,date],[],[],....]
            ticket:char
            name_id:char
            name:char
            date:char
    :return:
        inset count:int
    """
    try:
        cnn = pymysql.connect (user='monitoring',
                               passwd='server.mysql',
                               host='xxxxx',
                               db="xxxx",
                               charset='utf8')
        cur = cnn.cursor ()
        print("input data count :",len(data))
        SQL = 'INSERT INTO vote(ticket,name_id, name, date) VALUES (%s,%s,%s,%s)'
        ret = cur.executemany (SQL,data)
        cur.close ()
        cnn.commit ()
        cnn.close ()
    except:
        return -1
    return ret


def selectsql():
    cnn = pymysql.connect (user='monitoring',
                           passwd='server.mysql',
                           host='xxxxx',
                           db="xxxx",
                           charset='utf8')
    cur = cnn.cursor ()
    SQL = "SELECT COUNT(*) from vote"
    ret1 = cur.execute (SQL)
    ret2 = cur.fetchall ()
    cur.close ()
    cnn.close ()
    return ret2

if __name__ == '__main__':
    # try:
    #     if path.exists(argv[1]) == False:
    #         print ("[ERROR] file not found. Please enter the correct file")
    #         exit(1)
    #     FILE = argv[1]
    # except:
    #     print ("[ERROR] Please input command")

    #data = file2data (FILE)
    #ret = data2exesql (data)
    #print(data)
    #print ("SQL影响行数：",ret)

    ret = selectsql()
    print(ret[0][0])


