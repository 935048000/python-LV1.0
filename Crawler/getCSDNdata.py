"""

获取个人的CSND博客数据

取总阅读量和排名

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from re import sub
from time import sleep

while 1:
    html = urlopen("http://blog.csdn.net/chenvast")
    bsObj = BeautifulSoup (html, "html.parser")
    userInfoObj = bsObj.find("div", {"class":"content clearfix"})
    
    data = userInfoObj.find("aside")
    data = data.find("div", {"class":"interflow clearfix"})
    dataString = data.get_text()
    dataList = dataString.strip("\n").split("\n")
    TotalPV = dataList[1]
    Ranking = dataList[13]
    TotalPV = sub(",","",TotalPV)
    Ranking = sub(",","",Ranking)
    
    
    nowtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nowdate = datetime.now().strftime("%Y-%m-%d")
    
    # 文件名：data_日期.csv
    filename = "data_"+ nowdate+".csv"
    
    # 文本格式：时间，总访问量，排名
    filedata = nowtime+","+TotalPV+","+Ranking+"\n"
    
    with open (filename, "a") as f:
        f.write (filedata)
    sleep(600)





