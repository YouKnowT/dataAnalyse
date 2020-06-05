from flask import Flask,render_template
import csv
import jieba    #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud     #词云
from PIL import Image       #图片处理
import numpy as np
app = Flask(__name__)


@app.route('/')
def index():
    # Map=['澳门特别行政区','香港特别行政区','内蒙古自治区','宁夏回族自治区','新疆维吾尔自治区','西藏自治区','广西壮族自治区','云南省','甘肃省','台湾省','福建省','贵州省','浙江省','海南省','广东省','上海','北京','天津','重庆','黑龙江省','吉林省','辽宁省','江苏省','山东省','安徽省','河北省','河南省','湖北省','湖南省','江西省','陕西省','山西省','四川省','青海省']
    return render_template('Map.html')

@app.route('/Beijing')
def Beijing():
    with open(r"D:\pylearning\dataAnalyse\dataAnalyse\北京成交房源数据表.csv","r") as f:
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

    return render_template('Beijing.html',ran=ran,l=l,datalist=datalist)

@app.route('/BeijingTable')
def BeijingTable():
    with open(r"D:\pylearning\dataAnalyse\dataAnalyse\北京成交房源数据表.csv","r") as f:
        # ran=['<200','201-400','401-600','601-800','801-1000','>1000']    #成交金额范围
        # l=[0,0,0,0,0,0] #各成交金额范围的数量
        datalist=list(csv.reader(f))
    f.close()
    return render_template('BeijingTable.html',datalist=datalist)


@app.route('/Shanghai')
def Shanghai():
    with open(r"D:\pylearning\dataAnalyse\dataAnalyse\上海成交房源数据表.csv","r") as f:
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

    return render_template('Shanghai.html',l=l)
@app.route('/ShanghaiTable')
def ShanghaiTable():
    with open(r"D:\pylearning\dataAnalyse\dataAnalyse\上海成交房源数据表.csv","r") as f:
        # ran=['<200','201-400','401-600','601-800','801-1000','>1000']    #成交金额范围
        # l=[0,0,0,0,0,0] #各成交金额范围的数量
        datalist=list(csv.reader(f))
    f.close()
    return render_template('ShanghaiTable.html',datalist=datalist)



@app.route('/Tianjin')
def Tianjin():
    return render_template('Tianjin.html')

@app.route('/Chongqing')
def Chongqing():
    with open(r"D:\pylearning\dataAnalyse\dataAnalyse\重庆成交房源数据表.csv","r") as f:
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

    return render_template('Chongqing.html',l=l)
@app.route('/ChongqingTable')
def ChongqingTable():
    with open(r"D:\pylearning\dataAnalyse\dataAnalyse\重庆成交房源数据表.csv","r") as f:
        # ran=['<200','201-400','401-600','601-800','801-1000','>1000']    #成交金额范围
        # l=[0,0,0,0,0,0] #各成交金额范围的数量
        datalist=list(csv.reader(f))
    f.close()
    return render_template('ChongqingTable.html',datalist=datalist)



if __name__ == '__main__':
    app.run()
