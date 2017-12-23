#coding=utf-8
from sys import argv
from os import path
import pygal
from datetime import datetime, timedelta


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
        tickte1:官微的票数
        tickte2：官博的票数
        x_date：X轴的时间点
        link_name：折线的线名
    """
    # 官微
    data1 = []
    for x in data:
        if x[1] == 74:
            data1.append(x)


    tickte1 = []
    x_date = []
    for x1 in data1:
        tickte1.append (x1[0])
        x_date.append (x1[3][11:])
    # print(data1)

    # 官博
    data2 = []
    for y in data:
        if y[1] == 73:
            data2.append(y)

    tickte2 = []
    for y1 in data2:
        tickte2.append(y1[0])

    # 线名
    link_name = []
    link_name.append (data1[1][2])
    link_name.append (data2[1][2])

    return tickte1,tickte2,x_date,link_name



def getSVG(tickte1,tickte2,x_date,link_name,Ddate,svgname):
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
    line_chart.add(link_name[0],  tickte1)
    line_chart.add(link_name[1],  tickte2)
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

    # FILE = "./data_2017-12-21.txt"
    data = getdata(FILE)
    tickte1, tickte2, x_date, link_name = data2list(data)
    Ddate = FILE[:-4]
    Ddate = Ddate[-10:]
    SVGname = "%s.svg"% Ddate
    getSVG (tickte1, tickte2, x_date, link_name, Ddate, SVGname)
