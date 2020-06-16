#-*- codeing =utf-8 -*-
#@Time:2020/6/8 12:13 
#@Author: Demogorgon_Moriarty
#@File:getData.py
#@Software:PyCharm
# -*- coding:utf-8 -*-
import requests
import re

from bs4 import BeautifulSoup
from lxml import etree
import urllib.error,urllib.request
import sqlite3

findTitle=re.compile(r'target="_blank">(.*)</a></div>')         #房源标题
findIcon=re.compile(r'<span class="houseIcon"></span>(.*?)</div>')#houseIcon
findTotalprice=re.compile(r'<div class="totalPrice"><span class="number">(.*?)</span>')#总价
findDate=re.compile(r'<div class="dealDate">(.*)</div><div class="totalPrice">')#成交日期
findUnitprice=re.compile(r'<div class="unitPrice"><span class="number">(.*?)</span>')#单价
findPositionIcon=re.compile(r'<span class="positionIcon"></span>(.*)</div><div class="source">')#positionIcon
# findDescripe=re.compile(r'<span class="goodhouse_tag tagBlock">(.*)</span></div><div class="flood">')       #房源标签
# findType=re.compile(r'.*?</i>(.*?)<span',re.S)
# findFloor=re.compile(r'.*?</i>(.*?)</span>',re.S)
# findSquare=re.compile(r'.*?</i>(.*?)㎡',re.S)
# findMoney=re.compile(r'<span>单价(\d*)元/平米</span>')           #房源价格
# findImage = re.


# urllib.disable_warnings()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Connection': 'close',
}





def main():
    print("开始执行\n")
    baseurl="https://wz.lianjia.com/chengjiao/pg"
    datalist=getData(baseurl)
    dbpath = "houseMessage.db"
    #askURL("https://bj.lianjia.com/zufang/")
    save2DB(datalist,dbpath)


def getData(baseurl):
    print("开始执行1\n")
    datalist=[]
    for page in range(64):
        print("第%d页\n" % page)
        url = baseurl + str(page)
        html=askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        print("开始执行7\n")
        for item in soup.find_all('div',class_='info'):
            print("开始执行8\n")
            data=[]
            item=str(item)


            title=re.findall(findTitle,item)[0]
            list1=re.split(r'[ ]',title)
            # print(list1)
            if len(list1)==3:
                data.append(list1[0].strip())
                data.append(list1[1].strip())
                data.append(list1[2].strip())
            elif len(list1)==2:
                data.append(list1[0].strip())
                data.append(list1[1].strip())
                data.append('N')
            elif len(list1)==1:
                data.append(list1[0].strip())
                data.append('N')
                data.append('N')
            elif len(list1)==0:
                data.append('N')
                data.append('N')
                data.append('N')

            # print(findUrl)
            icon=re.findall(findIcon,item)[0]
            # print(link)
            icon=re.sub(' ','',icon)
            list2=re.split(r'[|]',icon)
            # print(list2)
            data.append(list2[0].strip())
            data.append(list2[1].strip())


            # print(re.findall(findTotalprice,item))

            if re.findall(findTotalprice,item)==[]:
                print("continue")
                continue
            totalprice=re.findall(findTotalprice,item)[0]
            # if totalprice=='':
            #     continue
            # print(des)
            data.append(totalprice)


            unitprice=re.findall(findUnitprice,item)[0]
            # if unitprice=='':
            #     continue
            data.append(unitprice)

            date=re.findall(findDate,item)[0]
            data.append(date)

            positionicon=re.findall(findPositionIcon,item)[0]
            list3=re.split(r'[ ]',positionicon)
            print(list3)
            data.append(list3[0].strip())
            data.append(list3[1].strip())

            print(data)


            datalist.append(data)



            print("开始执行9\n")



    return datalist







def askURL(url):
    head={  #模拟浏览器头部信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    #用户代理：告诉豆瓣可以接受什么水平的文件内容
    request=urllib.request.Request(url=url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
       # print(e)
        if hasattr(e,"reason"):
            print(e.reason)
    print("开始执行3\n")

    return html





#数据库操作

def save2DB(datalist, dbpath):
    print("开始执行4\n")
    initDB(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        if len(data)!=10:
            continue
        for index in range(len(data)):
            data[index] = '"' + str(data[index]) + '"'
        sql = '''
            insert into Wenzhou
            (hname,htype,square,direction,degree,totalprice,price,hdata,hfloor,info)values (%s)
            ''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print("...")


def initDB(dbpath):
    # print("开始执行5\n")
    sql = '''
                create table Wenzhou
                (
                id integer primary key autoincrement,
                hname varchar ,
                htype varchar ,
                square varchar ,
                direction varchar ,
                degree varchar ,
                totalprice numeric ,
                price numeric ,
                hdata varchar ,
                hfloor varchar ,
                info text
                );
            '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print("init success")




#主函数调用
if __name__ == '__main__':
    main()