from flask import Flask,render_template,request,jsonify
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


@app.route('/Shandong')
def Shandong():
    # Map=['澳门特别行政区','香港特别行政区','内蒙古自治区','宁夏回族自治区','新疆维吾尔自治区','西藏自治区','广西壮族自治区','云南省','甘肃省','台湾省','福建省','贵州省','浙江省','海南省','广东省','上海','北京','天津','重庆','黑龙江省','吉林省','辽宁省','江苏省','山东省','安徽省','河北省','河南省','湖北省','湖南省','江西省','陕西省','山西省','四川省','青海省']
    return render_template('Shandong.html')

@app.route('/Beijing',methods={"POST","GET"})
def Beijing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
           select * from Beijing
           '''
    sql1 = f'select * from Beijing limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()


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


    return render_template('Beijing.html',count=count,count1=count1,ran=ran,l=l,ll=ll,
                           datalist=datalist,sum=sum,datalist1=datalist1)


@app.route('/BeijingTableData',methods={"POST","GET"})
def BeijingTableData():
    values = request.values
    page = values.get("page",1,int)
    size = values.get("limit",10,int)
    offset = size * page
    print(values)
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
    return jsonify(datalist)




@app.route('/Shanghai', methods={"POST", "GET"})
def Shanghai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Shanghai
               '''
    sql1 = f'select * from Shaghai limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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
    return render_template('Shanghai.html',count=count,count1=count1,ran=ran,l=l,ll=ll,
                           datalist=datalist,sum=sum,datalist1=datalist1)
@app.route('/SanghaiTableData',methods={"POST","GET"})
def ShanghaiTableData():
    values = request.values
    page = values.get("page",1,int)
    size = values.get("limit",10,int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Shanghai limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Chongqing', methods={"POST", "GET"})
def Chongqing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Chongqing
               '''
    sql1 = f'select * from Chongqing limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Chongqing.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ChongqingTableData', methods={"POST", "GET"})
def ChongqingTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Chongqing limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Fuzhou', methods={"POST", "GET"})
def Fuzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Fuzhou
               '''
    sql1 = f'select * from Fuzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Fuzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/FuzhouTableData', methods={"POST", "GET"})
def FuzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Fuzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Shenyang', methods={"POST", "GET"})
def Shenyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Shenyang
               '''
    sql1 = f'select * from Shenyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Shenyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ShenyangTableData', methods={"POST", "GET"})
def ShenyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Shenyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Hefei', methods={"POST", "GET"})
def Hefei():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Hefei
               '''
    sql1 = f'select * from Hefei limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Hefei.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/HefeiTableData', methods={"POST", "GET"})
def HefeiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Hefei limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Guangzhou', methods={"POST", "GET"})
def Guangzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Guangzhou
               '''
    sql1 = f'select * from Guangzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Guangzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/GuangzhouTableData', methods={"POST", "GET"})
def GuangzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Guangzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Huangzhou', methods={"POST", "GET"})
def Huangzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Huangzhou
               '''
    sql1 = f'select * from Huangzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Huangzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/HuangzhouTableData', methods={"POST", "GET"})
def HuangzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Huangzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)





@app.route('/Chengdu', methods={"POST", "GET"})
def Chengdu():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Chengdu
               '''
    sql1 = f'select * from Chengdu limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Chengdu.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ChengduTableData', methods={"POST", "GET"})
def ChengduTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Chengdu limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Shijiazhuang', methods={"POST", "GET"})
def Shijiazhuang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Shijiazhuang
               '''
    sql1 = f'select * from Shijiazhuang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Shijiazhuang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ShijiazhuangTableData', methods={"POST", "GET"})
def ShijiazhuangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Shijiazhuang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Changsha', methods={"POST", "GET"})
def Changsha():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Changsha
               '''
    sql1 = f'select * from Changsha limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Changsha.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ChangshaTableData', methods={"POST", "GET"})
def ChangshaTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Changsha limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)




#3

@app.route('/Dongguan', methods={"POST", "GET"})
def Dongguan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Dongguan
               '''
    sql1 = f'select * from Dongguan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Dongguan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/DongguanTableData', methods={"POST", "GET"})
def DongguanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Dongguan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Foshan', methods={"POST", "GET"})
def Foshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Foshan
               '''
    sql1 = f'select * from Foshan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Foshan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/FoshanTableData', methods={"POST", "GET"})
def FoshanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Foshan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Haikou', methods={"POST", "GET"})
def Haikou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Haikou
               '''
    sql1 = f'select * from Haikou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Haikou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/HaikouTableData', methods={"POST", "GET"})
def HaikouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Haikou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Kunming', methods={"POST", "GET"})
def Kunming():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Kunming
               '''
    sql1 = f'select * from Kunming limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Kunming.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/KunmingTableData', methods={"POST", "GET"})
def KunmingTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Kunming limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Xiamen', methods={"POST", "GET"})
def Xiamen():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Xiamen
               '''
    sql1 = f'select * from Xiamen limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Xiamen.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/XiamenTableData', methods={"POST", "GET"})
def XiamenTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Xiamen limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Wuxi', methods={"POST", "GET"})
def Wuxi():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Wuxi
               '''
    sql1 = f'select * from Wuxi limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Wuxi.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/WuxiTableData', methods={"POST", "GET"})
def WuxiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Wuxi limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Wuhan', methods={"POST", "GET"})
def Wuhan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Wuhan
               '''
    sql1 = f'select * from Wuhan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Wuhan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/WuhanTableData', methods={"POST", "GET"})
def WuhanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Wuhan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)




#4
@app.route('/Beihai', methods={"POST", "GET"})
def Beihai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Beihai
               '''
    sql1 = f'select * from Beihai limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Beihai.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/BeihaiTableData', methods={"POST", "GET"})
def BeihaiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Beihai limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Jiangmen', methods={"POST", "GET"})
def Jiangmen():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Jiangmen
               '''
    sql1 = f'select * from Jiangmen limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Jiangmen.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/JiangmenTableData', methods={"POST", "GET"})
def JiangmenTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Jiangmen limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Langfang', methods={"POST", "GET"})
def Langfang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Langfang
               '''
    sql1 = f'select * from Langfang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Langfang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/LangfangTableData', methods={"POST", "GET"})
def LangfangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Langfang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Liuzhou', methods={"POST", "GET"})
def Liuzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Liuzhou
               '''
    sql1 = f'select * from Liuzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Liuzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/LiuzhouTableData', methods={"POST", "GET"})
def LiuzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Liuzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Maanshan', methods={"POST", "GET"})
def Maanshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Maanshan
               '''
    sql1 = f'select * from Maanshan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Maanshan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/MaanshanTableData', methods={"POST", "GET"})
def MaanshanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Maanshan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Nanjing', methods={"POST", "GET"})
def Nanjing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Nanjing
               '''
    sql1 = f'select * from Nanjing limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Nanjing.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/NanjingTableData', methods={"POST", "GET"})
def NanjingTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Nanjing limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Nanning', methods={"POST", "GET"})
def Nanning():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Nanning
               '''
    sql1 = f'select * from Nanning limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Nanning.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/NanningTableData', methods={"POST", "GET"})
def NanningTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Nanning limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Quanzhou', methods={"POST", "GET"})
def Quanzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Quanzhou
               '''
    sql1 = f'select * from Quanzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Quanzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/QuanzhouTableData', methods={"POST", "GET"})
def QuanzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Quanzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Shenzhen', methods={"POST", "GET"})
def Shenzhen():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Shenzhen
               '''
    sql1 = f'select * from Shenzhen limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Shenzhen.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ShenzhenTableData', methods={"POST", "GET"})
def ShenzhenTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Shenzhen limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Suzhou', methods={"POST", "GET"})
def Suzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Suzhou
               '''
    sql1 = f'select * from Suzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Suzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/SuzhouTableData', methods={"POST", "GET"})
def SuzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Suzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Tangshan', methods={"POST", "GET"})
def Tangshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Tangshan
               '''
    sql1 = f'select * from Tangshan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Suzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/TangshanTableData', methods={"POST", "GET"})
def TangshanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Tangshan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Xinxiang', methods={"POST", "GET"})
def Xinxiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Xinxiang
               '''
    sql1 = f'select * from Xinxiang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Xinxiang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/XinxiangTableData', methods={"POST", "GET"})
def XinxiangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Xinxiang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Yueyang', methods={"POST", "GET"})
def Yueyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Yueyang
               '''
    sql1 = f'select * from Yueyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Yueyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/YueyangTableData', methods={"POST", "GET"})
def YueyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Yueyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Zhanjiang', methods={"POST", "GET"})
def Zhanjiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zhanjiang
               '''
    sql1 = f'select * from Zhanjiang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zhanjiang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ZhanjiangTableData', methods={"POST", "GET"})
def ZhanjiangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zhanjiang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Zhangjiakou', methods={"POST", "GET"})
def Zhangjiakou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zhangjiakou
               '''
    sql1 = f'select * from Zhangjiakou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zhangjiakou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ZhangjiakouTableData', methods={"POST", "GET"})
def ZhangjiakouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zhangjiakou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Zhangzhou', methods={"POST", "GET"})
def Zhangzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zhangzhou
               '''
    sql1 = f'select * from Zhangzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zhangzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ZhangzhouTableData', methods={"POST", "GET"})
def ZhangzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zhangzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


#5

@app.route('/Changzhou', methods={"POST", "GET"})
def Changzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Changzhou
               '''
    sql1 = f'select * from Changzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Changzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ChangzhouTableData', methods={"POST", "GET"})
def ChangzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Changzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Dazhou', methods={"POST", "GET"})
def Dazhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Dazhou
               '''
    sql1 = f'select * from Dazhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Dazhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/DazhouTableData', methods={"POST", "GET"})
def DazhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Dazhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Dalian', methods={"POST", "GET"})
def Dalian():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Dalian
               '''
    sql1 = f'select * from Dalian limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Dalian.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/DalianTableData', methods={"POST", "GET"})
def DalianTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Dalian limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Dandong', methods={"POST", "GET"})
def Dandong():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Dandong
               '''
    sql1 = f'select * from Dandong limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Dandong.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/DandongTableData', methods={"POST", "GET"})
def DandongTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Dandong limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Guilin', methods={"POST", "GET"})
def Guilin():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Guilin
               '''
    sql1 = f'select * from Guilin limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Guilin.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/GuilinTableData', methods={"POST", "GET"})
def GuilinTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Guilin limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Haerbin', methods={"POST", "GET"})
def Haerbin():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Haerbin
               '''
    sql1 = f'select * from Haerbin limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Haerbin.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/HaerbinTableData', methods={"POST", "GET"})
def HaerbinTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Haerbin limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Huaian', methods={"POST", "GET"})
def Huaian():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Huaian
               '''
    sql1 = f'select * from Huaian limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Huaian.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/HuaianTableData', methods={"POST", "GET"})
def HuaianTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Huaian limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Huangshan', methods={"POST", "GET"})
def Huangshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Huangshan
               '''
    sql1 = f'select * from Huangshan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Huangshan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/HuangshanTableData', methods={"POST", "GET"})
def HuangshanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Huangshan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Jilin', methods={"POST", "GET"})
def Jilin():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Jilin
               '''
    sql1 = f'select * from Jilin limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Jilin.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/JilinTableData', methods={"POST", "GET"})
def JilinTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Jilin limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Jiujiang', methods={"POST", "GET"})
def Jiujiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Jiujiang
               '''
    sql1 = f'select * from Jiujiang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Jiujiang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/JiujiangTableData', methods={"POST", "GET"})
def JiujiangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Jiujiang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Luoyang', methods={"POST", "GET"})
def Luoyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Luoyang
               '''
    sql1 = f'select * from Luoyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Luoyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/LuoyangTableData', methods={"POST", "GET"})
def LuoyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Luoyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Nantong', methods={"POST", "GET"})
def Nantong():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Nantong
               '''
    sql1 = f'select * from Nantong limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Nantong.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/NantongTableData', methods={"POST", "GET"})
def NantongTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Nantong limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Qingdao', methods={"POST", "GET"})
def Qingdao():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Qingdao
               '''
    sql1 = f'select * from Qingdao limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Qingdao.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/QingdaoTableData', methods={"POST", "GET"})
def QingdaoTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Qingdao limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Shangrao', methods={"POST", "GET"})
def Shangrao():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Shangrao
               '''
    sql1 = f'select * from Shangrao limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Shangrao.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/ShangraoTableData', methods={"POST", "GET"})
def ShangraoTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Shangrao limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Weihai', methods={"POST", "GET"})
def Weihai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Weihai
               '''
    sql1 = f'select * from Weihai limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Weihai.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/WeihaiTableData', methods={"POST", "GET"})
def WeihaiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Weihai limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Weifang', methods={"POST", "GET"})
def Weifang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Weifang
               '''
    sql1 = f'select * from Weifang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Weifang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/WeifangTableData', methods={"POST", "GET"})
def WeifangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Weifang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Xiangyang', methods={"POST", "GET"})
def Xiangyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Xiangyang
               '''
    sql1 = f'select * from Xiangyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Xiangyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/XiangyangTableData', methods={"POST", "GET"})
def XiangyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Xiangyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Xuchang', methods={"POST", "GET"})
def Xuchang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Xuchang
               '''
    sql1 = f'select * from Xuchang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Xuchang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/XuchangTableData', methods={"POST", "GET"})
def XuchangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Xuchang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Yancheng', methods={"POST", "GET"})
def Yancheng():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Yancheng
               '''
    sql1 = f'select * from Yancheng limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Yancheng.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/YanchengTableData', methods={"POST", "GET"})
def YanchengTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Yancheng limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Yinchuan', methods={"POST", "GET"})
def Yinchuan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Yinchuan
               '''
    sql1 = f'select * from Yinchuan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Yinchuan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/YinchuanTableData', methods={"POST", "GET"})
def YinchuanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Yinchuan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Zhenzhou', methods={"POST", "GET"})
def Zhenzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zhenzhou
               '''
    sql1 = f'select * from Zhenzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zhenzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ZhenzhouTableData', methods={"POST", "GET"})
def ZhenzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zhenzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


#6

@app.route('/Baoji', methods={"POST", "GET"})
def Baoji():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Baoji
               '''
    sql1 = f'select * from Baoji limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Baoji.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/BaojiTableData', methods={"POST", "GET"})
def BaojiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Baoji limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Baoding', methods={"POST", "GET"})
def Baoding():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Baoding
               '''
    sql1 = f'select * from Baoding limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Baoding.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/BaodingTableData', methods={"POST", "GET"})
def BaodingTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Baoding limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Changde', methods={"POST", "GET"})
def Changde():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Changde
               '''
    sql1 = f'select * from Changde limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Changde.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ChangdeTableData', methods={"POST", "GET"})
def ChangdeTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Changde limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Chifeng', methods={"POST", "GET"})
def Chifeng():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Chifeng
               '''
    sql1 = f'select * from Chifeng limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Chifeng.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ChifengTableData', methods={"POST", "GET"})
def ChifengTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Chifeng limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Guiyang', methods={"POST", "GET"})
def Guiyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Guiyang
               '''
    sql1 = f'select * from Guiyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Guiyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/GuiyangTableData', methods={"POST", "GET"})
def GuiyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Guiyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Hanzhong', methods={"POST", "GET"})
def Hanzhong():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Hanzhong
               '''
    sql1 = f'select * from Hanzhong limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Hanzhong.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/HanzhongTableData', methods={"POST", "GET"})
def HanzhongTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Hanzhong limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Huhehaote', methods={"POST", "GET"})
def Huhehaote():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Huhehaote
               '''
    sql1 = f'select * from Huhehaote limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Huhehaote.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/HuhehaoteTableData', methods={"POST", "GET"})
def HuhehaoteTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Huhehaote limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Huzhou', methods={"POST", "GET"})
def Huzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Huzhou
               '''
    sql1 = f'select * from Huzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Huzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/HuzhouTableData', methods={"POST", "GET"})
def HuzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Huzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Jinan', methods={"POST", "GET"})
def Jinan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Jinan
               '''
    sql1 = f'select * from Jinan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Jinan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)


@app.route('/JinanTableData', methods={"POST", "GET"})
def JinanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Jinan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)



@app.route('/Jinhua', methods={"POST", "GET"})
def Jinhua():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Jinhua
               '''
    sql1 = f'select * from Jinhua limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Jinhua.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/JinhuaTableData', methods={"POST", "GET"})
def JinhuaTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Jinhua limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Lanzhou', methods={"POST", "GET"})
def Lanzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Lanzhou
               '''
    sql1 = f'select * from Lanzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Lanzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/LanzhouTableData', methods={"POST", "GET"})
def LanzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Lanzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Liangshan', methods={"POST", "GET"})
def Liangshan():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Liangshan
               '''
    sql1 = f'select * from Liangshan limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Liangshan.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/LiangshanTableData', methods={"POST", "GET"})
def LiangshanTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Liangshan limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Linyi', methods={"POST", "GET"})
def Linyi():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Linyi
               '''
    sql1 = f'select * from Linyi limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Linyi.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/LinyiTableData', methods={"POST", "GET"})
def LinyiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Linyi limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Mianyang', methods={"POST", "GET"})
def Mianyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Mianyang
               '''
    sql1 = f'select * from Mianyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Mianyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/MianyangTableData', methods={"POST", "GET"})
def MianyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Mianyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Ningbo', methods={"POST", "GET"})
def Ningbo():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Ningbo
               '''
    sql1 = f'select * from Ningbo limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Ningbo.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/NingboTableData', methods={"POST", "GET"})
def NingboTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Ningbo limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Shaoxing')
def Shaoxing():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Shaoxing
               '''
    sql1 = f'select * from Shaoxing limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Shaoxing.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ShaoxingTableData', methods={"POST", "GET"})
def ShaoxingTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Shaoxing limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Taizhou', methods={"POST", "GET"})
def Taizhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Taizhou
               '''
    sql1 = f'select * from Taizhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Taizhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/TaizhouTableData', methods={"POST", "GET"})
def TaizhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Taizhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Wenzhou', methods={"POST", "GET"})
def Wenzhou():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Wenzhou
               '''
    sql1 = f'select * from Wenzhou limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Wenzhou.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/WenzhouTableData', methods={"POST", "GET"})
def WenzhouTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Wenzhou limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Xianyang', methods={"POST", "GET"})
def Xianyang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Xianyang
               '''
    sql1 = f'select * from Xianyang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Xianyang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/XianyangTableData', methods={"POST", "GET"})
def XianyangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Xianyang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Yantai', methods={"POST", "GET"})
def Yantai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Yantai
               '''
    sql1 = f'select * from Yantai limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Yantai.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/YantaiTableData', methods={"POST", "GET"})
def YantaiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Yantai limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Zhenjiang', methods={"POST", "GET"})
def Zhenjiang():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zhenjiang
               '''
    sql1 = f'select * from Zhenjiang limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zhenjiang.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ZhenjiangTableData', methods={"POST", "GET"})
def ZhenjiangTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zhenjiang limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


@app.route('/Zhuhai', methods={"POST", "GET"})
def Zhuhai():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zhuhai
               '''
    sql1 = f'select * from Zhuhai limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zhuhai.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ZhuhaiTableData', methods={"POST", "GET"})
def ZhuhaiTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zhuhai limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)

@app.route('/Zibo', methods={"POST", "GET"})
def Zibo():
    count = 0
    count1 = 0
    datalist = []
    datalist1 = []
    datalist2 = []
    args = request.args
    page = args.get("page", 1, int)
    size = args.get("limit", 10, int)
    offset = size * page
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #     select totalprice,price,hdata from Fuzhou
    #     '''
    sql = '''
               select * from Zibo
               '''
    sql1 = f'select * from Zibo limit {size} offset {offset}'

    d = cur.execute(sql)
    for item in d:
        # count+=1
        datalist.append(item)
        # datalist1.append(item[1])
        # datalist2.append(item[2])
    d = cur.execute(sql1)
    for item in d:
        datalist1.append(item)
    cur.close()
    conn.close()

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

    return render_template('Zibo.html', count=count, count1=count1, ran=ran, l=l, ll=ll,
                           datalist=datalist, sum=sum, datalist1=datalist1)

@app.route('/ZiboTableData', methods={"POST", "GET"})
def ZiboTableData():
    values = request.values
    page = values.get("page", 1, int)
    size = values.get("limit", 10, int)
    offset = size * page
    print(values)
    datalist = []
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    # sql = '''
    #             select * from Beijing
    #             '''
    sql = f'select * from Zibo limit {size} offset {offset}'
    d = cur.execute(sql)
    for item in d:
        datalist.append(item)
    cur.close()
    conn.close()
    return jsonify(datalist)


if __name__ == '__main__':
    app.run()
