#!/usr/bin/env python  
# encoding: utf-8 
# @Author    : w2n1ck
# @Time      : 2018/3/23 下午4:51
# @Introduce :

line1 = 9000
line2 = 18000
line3 = 27000
line4 = 36000
line5 = 45000
line6 = 54000
line7 = 63000
line8 = 72000
line9 = 81000
line10 = 86635

with open('./url.txt', 'r') as f:
    line = f.readlines()
    print len(line)
    for i in range(line1):
        with open('./url-1.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line1,line2):
        with open('./url-2.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line2,line3):
        with open('./url-3.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line3,line4):
        with open('./url-4.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line4,line5):
        with open('./url-5.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line5,line6):
        with open('./url-6.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line6,line7):
        with open('./url-7.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line7,line8):
        with open('./url-8.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line8,line9):
        with open('./url-9.txt','a+') as _:
            _.write("%s" % line[i])
    for i in range(line9,line10):
        with open('./url-10.txt','a+') as _:
            _.write("%s" % line[i])