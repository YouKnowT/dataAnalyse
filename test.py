#-*- codeing =utf-8 -*-
#@Time:2020/6/8 11:36 
#@Author: Demogorgon_Moriarty
#@File:test.py
#@Software:PyCharm

import sqlite3
count=0
datalist1=[]
datalist2=[]
conn = sqlite3.connect("houseMessage.db")
cur = conn.cursor()
sql = '''
        select * from Fuzhou
       
         '''
d=cur.execute(sql)
for item in d:

    datalist1.append(item)


cur.close()
conn.close()
# print(datalist1)
sum=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ran=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for data in datalist1:
    if data[8] <= '2019.01.31':
        ran[0] += 1
        sum[0]+=data[7]
    elif data[8] >= '2019.02.01' and data[8] <= '2019.02.29':
        ran[1] += 1
        sum[1] += data[7]
    elif data[8] >= '2019.03.01' and data[8] <= '2019.03.31':
        ran[2] += 1
        sum[2] += data[7]
    elif data[8] > '2019.04.01' and data[8] <= '2019.04.30':
        ran[3] += 1
        sum[3] += data[7]
    elif data[8] > '2019.05.01' and data[8] <= '2019.05.31':
        ran[4] += 1
        sum[4] += data[7]
    elif data[8] > '2019.06.01' and data[8] <= '2019.06.30':
        ran[5] += 1
        sum[5] += data[7]
    elif data[8] >= '2019.07.01' and data[8] <= '2019.07.31':
        ran[6] += 1
        sum[6] += data[7]
    elif data[8] >= '2019.08.01' and data[8] <= '2019.08.31':
        ran[7] += 1
        sum[7] += data[7]
    elif data[8] >= '2019.09.01' and data[8] <= '2019.09.30':
        ran[8] += 1
        sum[8] += data[7]
    elif data[8] >= '2019.10.01' and data[8] <= '2019.10.31':
        ran[9] += 1
        sum[9] += data[7]
    elif data[8] >= '2019.11.01' and data[8] <= '2019.11.30':
        ran[10] += 1
        sum[10] += data[7]
    elif data[8] >= '2019.12.01' and data[8] <= '2019.12.31':
        ran[11] += 1
        sum[11] += data[7]
    elif data[8] >= '2020.01.01' and data[8] <= '2020.01.31':
        ran[12] += 1
        sum[12] += data[7]
    elif data[8] >= '2020.02.01' and data[8] <= '2020.02.29':
        ran[13] += 1
        sum[13] += data[7]
    elif data[8] >= '2020.03.01' and data[8] <= '2020.03.31':
        ran[14] += 1
        sum[14] += data[7]
    elif data[8] > '2020.04.01' and data[8] <= '2020.04.30':
        ran[15] += 1
        sum[15] += data[7]
    elif data[8] >= '2020.05.01' and data[8] <= '2020.05.31':
        ran[16] += 1
        sum[16] += data[7]
# for i in range(datalist1):
#     for data in datalist1:
#         if data > '2020.05.01':
#             print(data)
#             count+=1

# print(datalist2)

for i in range(0,17):
    sum[i]=sum[i]/ran[i]
print(ran)
print(sum)