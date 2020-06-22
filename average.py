#-*- codeing =utf-8 -*-
#@Time:2020/6/22 1:10 
#@Author: Demogorgon_Moriarty
#@File:average.py
#@Software:PyCharm

import sqlite3
def average():
    dbpath="houseMessage.db"
    db(dbpath)

def db(dbpath):
    sum=0
    datalist=[]
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
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
    for data in datalist:
        sum+=data[7]
    print(sum)
    a=len(datalist)
    print(a)
    print(sum/a)




if __name__ == '__main__':
        average()