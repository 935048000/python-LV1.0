#!/usr/bin/python
#coding=utf-8
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
# 
data = [((0,0),(1,1)) , ((5,5),(8,8)) ,((9,10),(11,12))]
 
drawing = Drawing(400,200)
 
lp = LinePlot()
#为LinePlot类设置一些相关属性
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = data
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green
 
drawing.add(lp)
drawing.add(String(250,150,'myline',fontsize = 14,fillcolor = colors.red))
renderPDF.drawToFile(drawing, 'lines.pdf' , 'myline')

# d = Drawing(100,100)
# s = String(50,50,'Hello world !',textAnchor='middle')
# d.add(s)
# renderPDF.drawToFile(d,'hello.pdf','A simple PDF file')