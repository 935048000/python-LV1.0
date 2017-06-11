#!/usr/bin/env python
# coding=utf-8


'''
与串行端口的数据通信
通过串行端口读写数据，典型场景就是和一些硬件设备打交道
'''


import serial

# Device name varies
ser = serial.Serial('/dev/tty.usbmodem641',
                    baudrate=9600,
                    bytesize=8,
                    parity='N',
                    stopbits=1)

ser.write(b'G1 X50 Y50\r\n')
resp = ser.readline()
























