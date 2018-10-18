"""
本脚本文件主要用于 MongoDB 数据导出


使用方法：
    使用本脚需要安装pymongo和bson库
    安装方法：pip install xxxx

    本脚本接受两个参数:
    1：文件存放路径（文件路径，不包括文件名）根据路径查找最新文件，取其最新的object Id，作为开始时间。
    2：开始日期 （格式为：yyyymmddhhmmss）根据提供的时间作为开始时间。
    例如：
    方法1：mongoDataExportScript.py /data/
    方法2：mongoDataExportScript.py /data/ 20181017083059



"""
import os
import time
import pandas as pd
import datetime
import sys
import pymongo
from bson.objectid import ObjectId


def datetime2objectId(from_datetime=None,
                      span_days=0,
                      span_hours=0,
                      span_minutes=0,
                      span_weeks=0):
    """
    根据时间手动生成一个objectid，此id不作为存储使用
    参数：
    from_datetime:datetime datetime时间
    span_days:int 偏移天（+:往前/-：往后）
    span_hours:int 偏移小时
    span_minutes:int 偏移分钟
    span_weeks:int 偏移周

    return: ObjectId
    """
    from_datetime = from_datetime + datetime.timedelta (days=span_days,
                                                        hours=span_hours - 8,
                                                        minutes=span_minutes,
                                                        weeks=span_weeks)
    
    return ObjectId.from_datetime (generation_time=from_datetime)


def range_search(start_timestamp, end_timestamp, ip, Uname, passwd, DB, Table):
    """
    读取指定时间内的MongoDB数据
    参数：
    start_timestamp:ObjectId 开始时间
    end_timestamp:ObjectId 结束时间
    ip:str 主机地址
    Uname:str 用户名
    passwd:str 密码
    DBname:str 数据库名
    Table:str 数据表名
    
    return: DataFrame
    """
    con = pymongo.MongoClient (ip, username=Uname, password=passwd)
    with con:
        db = con[DB]
        tableData = db[Table]
        
        return pd.DataFrame (list (tableData.find ({'_id': {'$lt': end_timestamp, '$gte': start_timestamp}})))


def newFile(dir):
    """
    从指定目录中找到最新修改的文件
    参数：
    dir：str 目录

    return:文件相对路径
    """
    # 列出目录下所有的文件
    filelist = os.listdir (dir)
    # print(filelist)
    # 对文件修改时间进行升序排列
    filelist.sort (key=lambda fn: os.path.getmtime (dir + '/' + fn))
    # 获取文件所在目录
    
    return filelist[-1]


def getLastId(filepath, filename):
    """获取CSV文件中的_id字段的最后一个值"""
    if filepath[-1] != "/":
        _filename = "%s%s%s" % (filepath, "/", filename)
    else:
        _filename = "%s%s" % (filepath, filename)
    data = pd.read_csv (_filename)
    
    return data['_id'].values[-1]


def datafileSave(data, filepath):
    """保存数据
    data:str 数据
    filepath:str 文件路径
    
    """
    data.to_csv (filepath)
    return 0


def id2time(object_id):
    """将mongodb的_id转化为时间
    
    return:datetime
    """
    date = time.localtime (int (object_id[:8], 16))
    # return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timeStamp))
    return datetime.datetime (date[0], date[1], date[2], date[3], date[4], date[5])


def id2timeString(object_id):
    """将mongodb的_id转化为时间
    
    return:strftime
    """
    object_id = str (object_id)
    date = time.localtime (int (object_id[:8], 16))
    
    # return time.strftime("%Y%m%d", time.localtime(date))
    return time.strftime ("%Y%m%d", date)


def main():
    """主函数"""
    # 连接参数
    IP = "xx"
    USER = "xx"
    PASSWD = "xx"
    DB = "xx"
    TABLE = "xx"
    
    # 程序接受参数1
    try:
        argv1 = sys.argv[1]
    except:
        # exit(1)
        pass
    
    # 程序接受参数2
    try:  # 指定第二个参数，使用从第二个参数指定的时间开始取数据
        argv2 = sys.argv[2]
        _time = datetime.datetime (int (argv2[:4]),
                                   int (argv2[4:6]),
                                   int (argv2[6:8]),
                                   int (argv2[8:10]),
                                   int (argv2[10:12]),
                                   int (argv2[12:14]))
    
    except:  # 没有第二个参数
        # 取最新文件
        _newFile = newFile (argv1)
        
        # 取最后一个 object_id
        _objectId = getLastId (argv1, _newFile)
        
        # 使用最后一个 object_id ，制作检索结束的 object_id 的时间
        _time = id2time (_objectId)
    
    # 从MongoDB中读取最后一个ID后一周的数据
    _startDate = datetime2objectId (from_datetime=_time)
    _endDate = datetime2objectId (from_datetime=_time, span_days=+7)
    MongoData = range_search (_startDate, _endDate, IP, USER, PASSWD, DB, TABLE)
    # MongoData = range_search (_startDate, _endDate, "127.0.0.1", "root", "root", "test", "app2")
    
    # 保存文件 文件名等于 路径+文件名+时间（yyyymmdd）
    fileName = "%s%s%s%s%s" % (argv1, "/", "mongoData_", id2timeString (_endDate), ".csv")
    datafileSave (MongoData, fileName)


if __name__ == '__main__':
    pass
    # 测试参数
    # argv1 = "./dataset/"
    # start time
    # start_timestamp = object_id_from_datetime(from_datetime=datetime.datetime(2018,10,17,15,0,0))
    # end time
    # end_timestamp = object_id_from_datetime(from_datetime=datetime.datetime(2018,10,17,18,0,0))
    # range_search(start_timestamp, end_timestamp)
    main ()
