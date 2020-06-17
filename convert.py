#-*- codeing =utf-8 -*-
#@Time:2020/6/8 7:31 
#@Author: Demogorgon_Moriarty
#@File:convert.py
#@Software:PyCharm

import sqlite3
import csv

def convert():
    with open(r"C:\Users\93991\Desktop\郑州全部数据去重1920.csv","r") as f:
        datalist=list(csv.reader(f))
    f.close()
    dbpath="houseMessage.db"
    db(datalist,dbpath)

def db(datalist,dbpath):
    # initDB(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index]='"'+str(data[index])+'"'
        sql='''
        insert into Zhengzhou
        (hname,htype,square,direction,degree,totalprice,price,hdata,hfloor,info)values (%s)
        '''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def initDB(dbpath):
    sql = '''
            create table Shangrao
            (
            id integer primary key autoincrement,
            hname varchar ,
            htype varchar ,
            square varchar ,
            totalprice numeric ,
            price varchar ,
            hdata varchar ,
            direction varchar ,
            degree varchar ,
            hfloor varchar ,
            info text
            );
        '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    convert()