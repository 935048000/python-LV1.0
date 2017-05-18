#!/bin/python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
def main():
    # 颜色列表
        colorList = ['b','g','r','c','m','y','k']
    # 共用的横坐标
        threadList = [1,2,4,8,10]
   # 设置横坐标和纵坐标的名称
        plt.xlabel('threads')
        plt.ylabel('concurrent')
          # 图的标题
        plt.title('concurrent test')
          # 要绘制的线的列表
        lines = []
        # 对应的线的名称
        titles = []
        # 第一根线的纵坐标
        dataList1 = [2,5,7,15,30]
        # 根据横坐标和纵坐标画第一根线
        line1 = plt.plot(threadList, dataList1)
        # 设置线的颜色宽度等
        plt.setp(line1, color=colorList[0], linewidth=2.0)
        # 线的名称
        titles.append('Linux')
        lines.append(line1)
          # 同理画第二根线
        dataList2 = [2,4,6,18,35]
        line2 = plt.plot(threadList, dataList2)
        plt.setp(line2, color=colorList[1], linewidth=2.0)
        titles.append('FreeBSD')
        lines.append(line2)
        plt.legend(lines, titles)
        plt.savefig('/home/workspace/test.png', dpi=120)
       #如果是pdf就,plt.savefig('/home/workspace/test.pdf')
if __name__ == '__main__':
    main()