from flask import Flask,render_template,request
# import csv
# import jieba    #分词
# from matplotlib import pyplot as plt    #绘图，数据可视化
# from wordcloud import WordCloud     #词云
# from PIL import Image       #图片处理
# import numpy as np
#
# from dataAnalyse.Cloud import text

app = Flask(__name__)
import sqlite3
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "houseMessage.db")

@app.route('/')
def index():
    # Map=['澳门特别行政区','香港特别行政区','内蒙古自治区','宁夏回族自治区','新疆维吾尔自治区','西藏自治区','广西壮族自治区','云南省','甘肃省','台湾省','福建省','贵州省','浙江省','海南省','广东省','上海','北京','天津','重庆','黑龙江省','吉林省','辽宁省','江苏省','山东省','安徽省','河北省','河南省','湖北省','湖南省','江西省','陕西省','山西省','四川省','青海省']
    return render_template('Map.html')

@app.route('/Beijing')
def Beijing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
           select * from Beijing
           '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Beijing.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/BeijingTable',methods={"POST","GET"})
def BeijingTable():
    args = request.args
    page = int(args.get("page"))
    size = int(args.get("size"))
    offset = size * page
    print(args)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Beijing limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('BeijingTable.html',datalist=datalist)


@app.route('/Shanghai')
def Shanghai():
    count = 0
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
                select totalprice from Shanghai
                '''
    d = cur.execute(sql)
    for item in d:
        count += 1
        datalist.append(item[0])
    cur.close()
    conn.close()
    print(datalist)

    ran = ['<200', '201-400', '401-600', '601-800', '801-1000', '>1000']  # 成交金额范围
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量
    for data in datalist:
        # print(type(data[6]))
        if data > 0 and data <= 200:
            l[0] += 1
        elif data > 200 and data <= 400:
            l[1] += 1
        elif data > 400 and data <= 600:
            l[2] += 1
        elif data > 600 and data <= 800:
            l[3] += 1
        elif data > 800 and data <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    return render_template('Shanghai.html',count=count,ran=ran,l=l)

@app.route('/ShanghaiTable')
def ShanghaiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
                    select * from Shanghai
                    '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ShanghaiTable.html',datalist=datalist)



@app.route('/Tianjin')
def Tianjin():
    return render_template('Tianjin.html')

@app.route('/Chongqing')
def Chongqing():
    count = 0
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
                    select totalprice from Chongqing
                    '''
    d = cur.execute(sql)
    for item in d:
        count += 1
        datalist.append(item[0])
    cur.close()
    conn.close()
    print(datalist)
    print(type(datalist[2]))
    ran = ['<200', '201-400', '401-600', '601-800', '801-1000', '>1000']  # 成交金额范围
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量
    for data in datalist:
        # print(type(data))
        if data > 0 and data <= 200:
            l[0] += 1
        elif data > 200 and data <= 400:
            l[1] += 1
        elif data > 400 and data <= 600:
            l[2] += 1
        elif data > 600 and data <= 800:
            l[3] += 1
        elif data > 800 and data <= 1000:
            l[4] += 1
        else:
            l[5] += 1

    return render_template('Chongqing.html',count=count,ran=ran,l=l)
@app.route('/ChongqingTable')
def ChongqingTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
                        select * from Chongqing
                        '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ChongqingTable.html',datalist=datalist)

@app.route('/Fuzhou')
def Fuzhou():
    count=0
    count1=0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql='''
    select * from Fuzhou
    '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    #成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l=[0,0,0,0,0,0] #各成交金额范围的数量,总价
    ll=[0,0,0,0,0]#单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1+=1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count+=1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Fuzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/FuzhouTable')
def FuzhouTable():
    datalist=[]
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Fuzhou
            '''
    d=cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('FuzhouTable.html',datalist=datalist)


@app.route('/Shenyang')
def Shenyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Shenyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Shenyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/ShenyangTable')
def ShenyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Shenyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ShenyangTable.html', datalist=datalist)


@app.route('/Hefei')
def Hefei():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Hefei
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Heifei.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/HefeiTable')
def HeifeiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Hefei
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HeifeiTable.html', datalist=datalist)


@app.route('/Guangzhou')
def Guangzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Guangzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Guangzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/GuangzhouTable')
def GuangzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Guangzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('GuangzhouTable.html', datalist=datalist)



@app.route('/Hangzhou')
def Hangzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Hangzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Hangzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/HangzhouTable')
def HangzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Hangzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HangzhouTable.html', datalist=datalist)





@app.route('/Chengdu')
def Chengdu():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Chengdu
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Chengdu.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/ChengduTable')
def ChengduTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Chengdu
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ChengduTable.html', datalist=datalist)



@app.route('/Shijiazhuang')
def Shijiazhuang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Shijiazhuang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Shijiazhuang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/ShijiazhuangTable')
def ShijiazhuangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Shijiazhuang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ShijiazhuangTable.html', datalist=datalist)



@app.route('/Changsha')
def Changsha():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Changsha
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Changsha.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)


@app.route('/ChangshaTable')
def ChangshaTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Changsha
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ChangshaTable.html', datalist=datalist)




#3

@app.route('/Dongguan')
def Dongguan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Dongguan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Dongguan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/DongguanTable')
def DongguanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Dongguan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('DongguanTable.html', datalist=datalist)

@app.route('/Foshan')
def Foshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Foshan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Foshan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/FoshanTable')
def FoshanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Foshan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('FoshanTable.html', datalist=datalist)


@app.route('/Haikou')
def Haikou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Haikou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Haikou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HaikouTable')
def HaikouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Haikou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HaikouTable.html', datalist=datalist)

@app.route('/Kunming')
def Kunming():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Kunming
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Kunming.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/KunmingTable')
def KunmingTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Kunming
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('KunmingTable.html', datalist=datalist)


@app.route('/Xiamen')
def Xiamen():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Xiamen
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Xiamen.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/XiamenTable')
def XiamenTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Xiamen
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('XiamenTable.html', datalist=datalist)

@app.route('/Wuxi')
def Wuxi():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Wuxi
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Wuxi.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/WuxiTable')
def WuxiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Wuxi
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('WuxiTable.html', datalist=datalist)

@app.route('/Wuhan')
def Wuhan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Wuhan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Wuhan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/WuhanTable')
def WuhanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Wuhan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('WuhanTable.html', datalist=datalist)




#4
@app.route('/Beihai')
def Beihai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Beihai
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Beihai.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/BeihaiTable')
def BeihaiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Beihai
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('BeihaiTable.html', datalist=datalist)

@app.route('/Jiangmen')
def Jiangmen():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Jiangmen
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Jiangmen.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/JiangmenTable')
def JiangmenTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Jiangmen
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('JiangmenTable.html', datalist=datalist)


@app.route('/Langfang')
def Langfang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Langfang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Langfang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/LangfangTable')
def LangfangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Langfang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('LangfangTable.html', datalist=datalist)

@app.route('/Liuzhou')
def Liuzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Liuzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Liuzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/LiuzhouTable')
def LiuzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Liuzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('LiuzhouTable.html', datalist=datalist)

@app.route('/Maanshan')
def Maanshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Maanshan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Maanshan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/MaanshanTable')
def MaanshanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Maanshan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('MaanshanTable.html', datalist=datalist)

@app.route('/Nanjing')
def Nanjing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Nanjing
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Nanjing.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/NanjingTable')
def NanjingTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Nanjing
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('NanjingTable.html', datalist=datalist)

@app.route('/Nanning')
def Nanning():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Nanning
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Nanning.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/NanningTable')
def NanningTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Nanning
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('NanningTable.html', datalist=datalist)

@app.route('/Quanzhou')
def Quanzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Quanzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Quanzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/QuanzhouTable')
def QuanzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Quanzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('QuanzhouTable.html', datalist=datalist)

@app.route('/Shenzhen')
def Shenzhen():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Shenzhen
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Shenzhen.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ShenzhenTable')
def ShenzhenTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Shenzhen
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ShenzhenTable.html', datalist=datalist)

@app.route('/Suzhou')
def Suzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Suzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Suzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/SuzhouTable')
def SuzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Suzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('SuzhouTable.html', datalist=datalist)


@app.route('/Tangshan')
def Tangshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Tangshan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Tangshan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/TangshanTable')
def TangshanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Tangshan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('TangshanTable.html', datalist=datalist)

@app.route('/Xinxiang')
def Xinxiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Xinxiang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Xinxiang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/XinxiangTable')
def XinxiangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Xinxiang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('XinxiangTable.html', datalist=datalist)

@app.route('/Yueyang')
def Yueyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Yueyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Yueyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/YueyangTable')
def YueyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Yueyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('YueyangTable.html', datalist=datalist)

@app.route('/Zhanjiang')
def Zhanjiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zhanjiang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zhanjiang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZhanjiangTable')
def ZhanjiangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Zhanjiang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZhanjiangTable.html', datalist=datalist)

@app.route('/Zhangjiakou')
def Zhangjiakou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zhangjiakou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zhangjiakou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZhangjiakouTable')
def ZhangjiakouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Zhangjiakou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZhangjiakouTable.html', datalist=datalist)

@app.route('/Zhangzhou')
def Zhangzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zhangzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zhangzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZhangzhouTable')
def ZhangzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Zhangzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZhangzhouTable.html', datalist=datalist)


#5

@app.route('/Changzhou')
def Changzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Changzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Changzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ChangzhouTable')
def ChangzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Changzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ChangzhouTable.html', datalist=datalist)

@app.route('/Dazhou')
def Dazhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Dazhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Dazhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/DazhouTable')
def DazhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Dazhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('DazhouTable.html', datalist=datalist)


@app.route('/Dlian')
def Dlian():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Dlian
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Dlian.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/DlianTable')
def DlianTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Dlian
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('DlianTable.html', datalist=datalist)

@app.route('/Dandong')
def Dandong():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Dandong
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Dandong.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/DandongTable')
def DandongTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Dandong
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('DandongTable.html', datalist=datalist)

@app.route('/Guilin')
def Guilin():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Guilin
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Guilin.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/GuilinTable')
def GuilinTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Guilin
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('GuilinTable.html', datalist=datalist)

@app.route('/Haerbin')
def Haerbin():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Haerbin
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Haerbin.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HaerbinTable')
def HaerbinTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Haerbin
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HaerbinTable.html', datalist=datalist)

@app.route('/Huaian')
def Huaian():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Huaian
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Huaian.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HuaianTable')
def HuaianTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Huaian
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HuaianTable.html', datalist=datalist)

@app.route('/Huangshi')
def Huangshi():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Huangshi
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Huangshi.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HuangshiTable')
def HuangshiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Huangshi
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HuangshiTable.html', datalist=datalist)

@app.route('/Jilin')
def Jilin():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Jilin
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Jilin.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/JilinTable')
def JilinTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Jilin
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('JilinTable.html', datalist=datalist)

@app.route('/Jiujiang')
def Jiujiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Jiujiang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Jiujiang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/JiujiangTable')
def JiujiangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Jiujiang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('JiujiangTable.html', datalist=datalist)


@app.route('/Luoyang')
def Luoyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Luoyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Luoyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/LuoyangTable')
def LuoyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Luoyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('LuoyangTable.html', datalist=datalist)

@app.route('/Nantong')
def Nantong():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Nantong
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Nantong.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/NantongTable')
def NantongTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Nantong
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('NantongTable.html', datalist=datalist)

@app.route('/Qingdao')
def Qingdao():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Qingdao
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Qingdao.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/QingdaoTable')
def QingdaoTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Qingdao
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('QingdaoTable.html', datalist=datalist)

@app.route('/Shangrao')
def Shangrao():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Shangrao
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Shangrao.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ShangraoTable')
def ShangraoTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Shangrao
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ShangraoTable.html', datalist=datalist)

@app.route('/Weihai')
def Weihai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Weihai
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Weihai.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/WeihaiTable')
def WeihaiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Weihai
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('WeihaiTable.html', datalist=datalist)

@app.route('/Weifang')
def Weifang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Weifang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Weifang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/WeifangTable')
def WeifangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Weifang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('WeifangTable.html', datalist=datalist)

@app.route('/Xiangyang')
def Xiangyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Xiangyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Xiangyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/XiangyangTable')
def XiangyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Xiangyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('XiangyangTable.html', datalist=datalist)

@app.route('/Xuchang')
def Xuchang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Xuchang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Xuchang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/XuchangTable')
def XuchangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Xuchang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('XuchangTable.html', datalist=datalist)

@app.route('/Yancheng')
def Yancheng():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Yancheng
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Yancheng.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/YanchengTable')
def YanchengTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Yancheng
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('YanchengTable.html', datalist=datalist)

@app.route('/Yinchuan')
def Yinchuan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Yinchuan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Yinchuan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/YinchuanTable')
def YinchuanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Yinchuan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('YinchuanTable.html', datalist=datalist)

@app.route('/Zhengzhou')
def Zhengzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zhengzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zhengzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZhengzhouTable')
def ZhengzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Zhengzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZhengzhouTable.html', datalist=datalist)


#6

@app.route('/Baoji')
def Baoji():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Baoji
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Baoji.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/BaojiTable')
def BaojiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Baoji
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('BaojiTable.html', datalist=datalist)

@app.route('/Baoding')
def Baoding():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Baoding
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Baoding.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/BaodingTable')
def BaodingTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Baoding
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('BaodingTable.html', datalist=datalist)


@app.route('/Changde')
def Changde():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Changde
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Changde.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ChangdeTable')
def ChangdeTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Changde
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ChangdeTable.html', datalist=datalist)

@app.route('/Chifeng')
def Chifeng():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Chifeng
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Chifeng.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ChifengTable')
def ChifengTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Chifeng
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ChifengTable.html', datalist=datalist)

@app.route('/Guiyang')
def Guiyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Guiyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Guiyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/GuiyangTable')
def GuiyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Guiyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('GuiyangTable.html', datalist=datalist)

@app.route('/Hanzhong')
def Hanzhong():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Hanzhong
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Hanzhong.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HanzhongTable')
def HanzhongTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Hanzhong
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HanzhongTable.html', datalist=datalist)

@app.route('/Huhehaote')
def Huhehaote():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Huhehaote
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Huhehaote.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HuhehaoteTable')
def HuhehaoteTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Huhehaote
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HuhehaoteTable.html', datalist=datalist)

@app.route('/Huzhou')
def Huzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Huzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Huzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/HuzhouTable')
def HuzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Huzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('HuzhouTable.html', datalist=datalist)

@app.route('/Jinan')
def Jinan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Jinan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Jinan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/JinanTable')
def JinanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Jinan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('JinanTable.html', datalist=datalist)

@app.route('/Jinhua')
def Jinhua():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Jinhua
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Jinhua.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/JinhuaTable')
def JinhuaTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Jinhua
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('JinhuaTable.html', datalist=datalist)


@app.route('/Lanzhou')
def Lanzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Lanzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Lanzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/LanzhouTable')
def LanzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Lanzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('LanzhouTable.html', datalist=datalist)

@app.route('/Liangshan')
def Liangshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Liangshan
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Liangshan.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/LiangshanTable')
def LiangshanTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Liangshan
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('LiangshanTable.html', datalist=datalist)

@app.route('/Linyi')
def Linyi():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Linyi
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Linyi.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/LinyiTable')
def LinyiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Linyi
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('LinyiTable.html', datalist=datalist)

@app.route('/Mianyang')
def Mianyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Mianyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Mianyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/MianyangTable')
def MianyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Mianyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('MianyangTable.html', datalist=datalist)

@app.route('/Ningbo')
def Ningbo():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Ningbo
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Ningbo.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/NingboTable')
def NingboTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Ningbo
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('NingboTable.html', datalist=datalist)

@app.route('/Shaoxing')
def Shaoxing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Shaoxing
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Shaoxing.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ShaoxingTable')
def ShaoxingTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Shaoxing
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ShaoxingTable.html', datalist=datalist)

@app.route('/Taizhou')
def Taizhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Taizhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Taizhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/TaizhouTable')
def TaizhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Taizhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('TaizhouTable.html', datalist=datalist)

@app.route('/Wenzhou')
def Wenzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Wenzhou
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Wenzhou.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/WenzhouTable')
def WenzhouTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Wenzhou
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('WenzhouTable.html', datalist=datalist)

@app.route('/Xianyang')
def Xianyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Xianyang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Xianyang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/XianyangTable')
def XianyangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Xianyang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('XianyangTable.html', datalist=datalist)

@app.route('/Yantai')
def Yantai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Yantai
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Yantai.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/YantaiTable')
def YantaiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Yantai
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('YantaiTable.html', datalist=datalist)

@app.route('/Zhenjiang')
def Zhenjiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zhenjiang
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zhenjiang.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZhenjiangTable')
def ZhenjiangTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Zhenjiang
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZhenjiangTable.html', datalist=datalist)

@app.route('/Zhuhai')
def Zhuhai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zhuhai
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zhuhai.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZhuhaiTable')
def ZhuhaiTable():
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql = '''
            select * from Zhuhai
            '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZhuhaiTable.html', datalist=datalist)

@app.route('/Zibo')
def Zibo():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
       select * from Zibo
       '''
    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    cur.close()
    conn.close()
    print(datalist2)

    ran = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 成交金额范围
    sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l = [0, 0, 0, 0, 0, 0]  # 各成交金额范围的数量,总价
    ll = [0, 0, 0, 0, 0]  # 单价
    for data in datalist:
        # print(type(data[6]))
        if data[6] > 0 and data[6] <= 200:
            l[0] += 1
        elif data[6] > 200 and data[6] <= 400:
            l[1] += 1
        elif data[6] > 400 and data[6] <= 600:
            l[2] += 1
        elif data[6] > 600 and data[6] <= 800:
            l[3] += 1
        elif data[6] > 800 and data[6] <= 1000:
            l[4] += 1
        else:
            l[5] += 1
    for data in datalist:
        if data[7] > 0 and data[7] <= 10000:
            ll[0] += 1
        elif data[7] > 10000 and data[7] <= 20000:
            ll[1] += 1
        elif data[7] > 20000 and data[7] <= 30000:
            ll[2] += 1
        elif data[7] > 30000 and data[7] <= 40000:
            ll[3] += 1
        else:
            ll[4] += 1

    for data in datalist:
        if data[8] <= '2019.01.31':
            count1 += 1
            ran[0] += 1
            sum[0] += data[7]
        elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
            count1 += 1
            ran[1] += 1
            sum[1] += data[7]
        elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
            count1 += 1
            ran[2] += 1
            sum[2] += data[7]
        elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
            count1 += 1
            ran[3] += 1
            sum[3] += data[7]
        elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
            count1 += 1
            ran[4] += 1
            sum[4] += data[7]
        elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
            count1 += 1
            ran[5] += 1
            sum[5] += data[7]
        elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
            count1 += 1
            ran[6] += 1
            sum[6] += data[7]
        elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
            count1 += 1
            ran[7] += 1
            sum[7] += data[7]
        elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
            count1 += 1
            ran[8] += 1
            sum[8] += data[7]
        elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
            count1 += 1
            ran[9] += 1
            sum[9] += data[7]
        elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
            count1 += 1
            ran[10] += 1
            sum[10] += data[7]
        elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
            count1 += 1
            ran[11] += 1
            sum[11] += data[7]
        elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
            count1 += 1
            ran[12] += 1
            sum[12] += data[7]
        elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
            count += 1
            ran[13] += 1
            sum[13] += data[7]
        elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
            count += 1
            ran[14] += 1
            sum[14] += data[7]
        elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
            count += 1
            ran[15] += 1
            sum[15] += data[7]
        elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
            count += 1
            ran[16] += 1
            sum[16] += data[7]
    for i in range(0, 17):
        sum[i] = sum[i] / ran[i]


    return render_template('Zibo.html',count=count,count1=count1,ran=ran,l=l,ll=ll,datalist=datalist,sum=sum)

@app.route('/ZiboTable',methods={"POST","GET"})
def ZiboTable():
    args=request.args
    page=int(args.get("page"))
    size=int(args.get("size"))
    offset= size * page
    print(args)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    sql=f'select * from Zibo limit {size} offset {offset}'
    # sql = '''
    #         select * from Zibo
    #         '''
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return render_template('ZiboTable.html', datalist=datalist)



if __name__ == '__main__':
    app.run()
