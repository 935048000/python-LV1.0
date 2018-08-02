"""

获取个人的CSND博客数据

取总阅读量和排名

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from re import sub
from time import sleep

# while 1:
html = urlopen("http://blog.csdn.net/chenvast")
bsObj = BeautifulSoup (html, "html.parser")
userInfoObj = bsObj.find ("ul", {"id": "blog_rank"})
userInfoObj2 = bsObj.find ("ul", {"id": "blog_statistics"})
dataString = userInfoObj.get_text () + userInfoObj2.get_text ()
dataList = dataString.strip("\n").split("\n")

# print(dataList[0],dataList[5],dataList[7],dataList[8],dataList[9])
# print(dataList[0][3:-1],dataList[5][4:-1],dataList[7][3:-1],dataList[8][3:-1],dataList[9][3:-1])

# 总访问量
TotalPV = dataList[0][3:-1]
# 排名
Ranking = dataList[5][4:-1]
# 原创
Original = dataList[7][3:-1]
# 转载
Retransmission = dataList[8][3:-1]
# 译文
Translation = dataList[9][3:-1]

# 时间
nowtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
nowdate = datetime.now().strftime("%Y-%m-%d")

# 文件名：data_日期.csv
filename = "data_"+ nowdate+".csv"

# 文本格式：时间，总访问量，排名
filedata = nowtime + "," + TotalPV + "," + Ranking + "," + Original + "," + Retransmission + "," + Translation + "\n"
# print(filedata)

# with open (filename, "a") as f:
#     f.write (filedata)
    # sleep(600)



