#-*- codeing =utf-8 -*-
#@Time:2020/5/27 12:02 
#@Author: Demogorgon_Moriarty
#@File:testBJ.py
#@Software:PyCharm

import jieba    #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud     #词云
from PIL import Image       #图片处理
import numpy as np
import csv
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/Beijing')
def Beijing():
    with open(r"D:\pylearning\dataAnalyse\北京成交房源数据表.csv","r") as f:
        ran=['<200','201-400','401-600','601-800','801-1000','>1000']    #成交金额范围
        l=[0,0,0,0,0,0] #各成交金额范围的数量
        datalist=list(csv.reader(f))
        for data in datalist:
            # print(type(data[3]))
            if int(data[3]) > 0 and int(data[3]) <= 200:
                l[0] += 1
            elif int(data[3]) > 200 and int(data[3]) <= 400:
                l[1] += 1
            elif int(data[3]) > 400 and int(data[3]) <= 600:
                l[2] += 1
            elif int(data[3]) > 600 and int(data[3]) <= 800:
                l[3] += 1
            elif int(data[3]) > 800 and int(data[3]) <= 1000:
                l[4] += 1
            else:
                l[5] += 1

    f.close()

    return render_template('./testTable.html',ran=ran,l=l,datalist=datalist)

if __name__ == '__main__':
    app.run()
