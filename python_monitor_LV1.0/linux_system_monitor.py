#!/usr/bin/python
#coding=utf-8
import sys  
import os
import datetime
import commands
  
import atexit  
import time   
import psutil 

#System
def systemstate():
        hostname = str(commands.getoutput('hostname'))
        systemload = str(commands.getoutput('uptime'))
        loadvalue = str(systemload[45:])
        print "主机名：",hostname
        print "系统运行时间 :",
        print datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        print "系统负载(1 min,5 min,15 min) ：",loadvalue
        return 0
    

#User
def users():
        print "远程主机登陆情况 ："
        userstate = psutil.users()
        n=0
        for i in userstate:
            #print userstate[n][2]
            if userstate[n][2] != "localhost" :
                print i
            else:
                pass
            n = n + 1
            #print i
        return 0


#CPU
def cpustate():  
        cpucountlogic = psutil.cpu_count()
        cpucountphy = psutil.cpu_count(logical=False)
        cpuuseds = psutil.cpu_percent(interval=0.5)
        cpuused = psutil.cpu_percent(percpu=True,interval=0.5)
        print "CPU物理总数 ：",cpucountphy
        print "CPU逻辑总数 ：",cpucountlogic
        print "CPU总的使用率: " , str(int(cpuuseds))+"%"
        j=0
        for i in cpuused:
            print "第 %1s 个CPU使用率: %2s" %(j,str(int(i)))+"%"
            j = j+1
        return 0



#memory
def memorystate():   
        mem = psutil.virtual_memory()  
        line = "内存使用率: %5s%% %6s/%s"%(  
            mem.percent,  
            str(int(mem.used/1024/1024))+"M",  
            str(int(mem.total/1024/1024))+"M"  
            )  
        return line


#disk
def diskstate():
        disktotal = psutil.disk_io_counters()
        diskroot = psutil.disk_usage('/')
        print "磁盘总体读写信息："
        print "总体读次数：",disktotal[0],"， 总体写次数：",disktotal[1],"， 总体读大小：",str(disktotal[2]/1024/1024/1024)+"G"\
            ,"， 总体写大小：",str(disktotal[3]/1024/1024/1024)+"G"
        print "\"/\"分区使用情况："
        print "使用率：",str(int(diskroot[3])),"%"", 使用比例：",str(int(diskroot[1]/1024/1024))+"M/",str(int(diskroot[0]/1024/1024))+"M"
#         line="分区使用情况：%7s %8s"%(
#             psutil.disk_io_counters(),
#             psutil.disk_usage('/')
#             )
#         return line
        return 0


#network
def networkstate():
#         line=(
#             psutil.net_io_counters(pernic=True)
#             )
#         return line
        network = psutil.net_io_counters(pernic=True)
        networkname0 = network.keys()[0]
        networkname1 = network.keys()[1]
        print "本机网卡列表：",network.keys()
        print "\"%s\"网卡信息 : "%network.keys()[0]
        print "总发包大小：",str(network[networkname0][0]/1024/1024)+"M",", 总收包大小：",str(network[networkname0][1]/1024/1024)+"M"\
        ,", 总发包数量：",network[networkname0][2],", 总收包数量：",network[networkname0][3]
        print "\"%s\"网卡信息 : "%network.keys()[1]
        print "总发包大小：",str(network[networkname1][0]/1024/1024)+"M",", 总收包大小：",str(network[networkname1][1]/1024/1024)+"M"\
        ,", 总发包数量：",network[networkname1][2],", 总收包数量：",network[networkname1][3]
        return 0

#window
def window():
    try:
            print "—————————————————————————————————————————————————————————————————"
            print "————————————————————————————  SYSTEM ———————————————————————————————"
            print "—————————————————————————————————————————————————————————————————"
            print systemstate()
            
            print "—————————————————————————————————————————————————————————————————"
            print "————————————————————————————  USER ———————————————————————————————"
            print "—————————————————————————————————————————————————————————————————"
            print users()
        
            print "—————————————————————————————————————————————————————————————————"
            print "————————————————————————————  CPU ———————————————————————————————"
            print "—————————————————————————————————————————————————————————————————"
            print cpustate()
        
            print "——————————————————————————————————————————————————————————————————"
            print "————————————————————————————  Memory ————————————————————————————————"
            print "———————————————————————————————————————————————————————————————————"
            print memorystate()
        
            print "—————————————————————————————————————————————————————————————————"
            print "————————————————————————————  Disk（磁盘信息） ———————————————"
            print "—————————————————————————————————————————————————————————————————"
            print diskstate() 
        
            print "—————————————————————————————————————————————————————————————————"
            print "———————————————————————————— NetWork(网卡信息) ———————————————————"
            print "—————————————————————————————————————————————————————————————————"
            print networkstate()
    except:
    	print ""
        print "[error] Forced out of the program"
    return 0

print window()
exit(0)







