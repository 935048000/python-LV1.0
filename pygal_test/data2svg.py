#coding=utf-8
from sys import argv
from os import path
import pygal
from datetime import datetime, timedelta
from operator import itemgetter

def getdata(FILE):
    """
    :param FILE:
        FILE --> file name
    :return list:
        file --> list
    """
    with open (FILE, "r", encoding="utf-8") as f:
        linedata = f.readlines ()
        lens = len (linedata)
        data = []
        for i in range (1,lens):
            line = linedata[i]
            line = line.strip ("\n").split (",")
            line[0] = int(line[0])
            line[1] = int(line[1])
            data.append (line)
    return data

# 获取文件日期
# print(data[1][3][:11])


def data2list(data):
    """
    :param data:
        data --> list
    :return: tickte1,tickte2,x_date,link_name
        tickte1:票数
        x_date：X轴的时间点
        link_name：折线的线名
    """
    # 线名
    link_name = []
    # 票数
    tickte = []
    # 时间
    x_date = []
    # 票名ID
    voteName = []

    voteID = data[-134:]
    voteID.sort(key=itemgetter(0),reverse=True)
    for k in voteID[:10]:
        voteName.append(k[1])
    voteName.append(73)


    for i in voteName:
        data2 = []
        for y in data:
            if y[1] == i:
                data2.append (y)

        link_name.append (data2[1][2])

        tickte2 = []
        for x in data2:
            tickte2.append (x[0])

            if len(x_date) <= 134:
                x_date.append (x[3][11:])

        tickte.append(tickte2)

    return tickte,x_date,link_name



def getSVG(tickte,x_date,link_name,Ddate,svgname):
    """
    :param tickte1: 官微的票数
    :param tickte2: 官博的票数
    :param x_date: X轴的时间点
    :param link_name: 折线的线名
    :param Ddate: 折线图名字
    :param svgname: svg文件名
    :return: int
    """
    my_config = pygal.Config()
    my_config.width = 1300

    line_chart = pygal.Line(my_config,x_label_rotation=90)

    title_name =  Ddate + '日的票数增长图'
    line_chart.title = title_name
    line_chart.x_labels = x_date
    for i,j in zip(tickte,link_name):
        line_chart.add(j,  i)


    # line_chart.add(link_name[1],  tickte2)
    line_chart.render_to_file(svgname)

    return 0



if __name__ == '__main__':
    try:
        if path.exists(argv[1]) == False:
            print ("[ERROR] file not found. Please enter the correct file")
            exit(1)
        FILE = argv[1]
    except:
        print ("[ERROR] Please input command")

    # FILE = "./data_2017-12-22.txt"
    data = getdata(FILE)
    tickte,x_date, link_name = data2list(data)
    Ddate = FILE[:-4]
    Ddate = Ddate[-10:]
    SVGname = "%s.svg"% Ddate
    getSVG (tickte,x_date, link_name, Ddate, SVGname)


