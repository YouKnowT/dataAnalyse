#-*- codeing =utf-8 -*-
#@Time:2020/5/27 2:17 
#@Author: Demogorgon_Moriarty
#@File:testCsv.py
#@Software:PyCharm

import csv

with open(r"D:\pylearning\dataAnalyse\北京成交房源数据表.csv","r") as f:
    l=[0,0,0,0,0,0]
    datalist=list(csv.reader(f))
    for data in datalist:
        # print(type(data[3]))
        if int(data[3])>0 and int(data[3])<=200:
            l[0]+=1
        elif int(data[3])>200 and int(data[3])<=400:
            l[1]+=1
        elif int(data[3])>400 and int(data[3])<=600:
            l[2]+=1
        elif int(data[3])>600 and int (data[3])<=800:
            l[3]+=1
        elif int(data[3])>800 and int(data[3])<=1000:
            l[4]+=1
        else:
            l[5]+=1
    print(l)
        # print(type(data[3]))
