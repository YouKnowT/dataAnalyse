#-*- codeing =utf-8 -*-
#@Time:2020/5/27 4:44 
#@Author: Demogorgon_Moriarty
#@File:Cloud.py
#@Software:PyCharm
import jieba    #分词
from matplotlib import pyplot as plt    #绘图，数据可视化
from wordcloud import WordCloud     #词云
from PIL import Image       #图片处理
import numpy as np      #矩阵运算
import sqlite3     #数据库

conn=sqlite3.connect("houseMessage.db")
cur=conn.cursor()
sql='''
    select * from shenyang
'''
# with open(r"D:\pylearning\dataAnalyse\重庆成交房源数据表.csv","r") as f:
#     sl=''
#     stringlist=csv.reader(f)
#     for s in stringlist:
#         for i in range(0,len(s)):
#             # sl+="'%s',"%s[i]
#             sl += s[i]
#
#     # print(stringlist)
#     # print(type(stringlist))
#     print(sl)
#     print(type(sl))

#准备词云所需文字和词
# con=sqlite3.connect('movie.db')
#
# cur=con.cursor()
# sql='''select introduction from movie '''
data=cur.execute(sql)
text=''
for item in data:
    for i in range(len(item)):
        text=text+str(item[i])
cur.close()
conn.close()

#

cut=jieba.cut(text)
string=' '.join(cut)
print(len(string))



img=Image.open(r'.\static\assets\img\shenyang.jpg')     #打开遮罩图片
image_array=np.array(img)   #将图片转换为数组
wc=WordCloud(
    background_color='white',
    mask=image_array,
    font_path="SIMYOU.TTF"            #字体所在位置：c:windows:font
)
wc.generate_from_text(string)


#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')     #是否显示坐标轴
# plt.show()      #显示生成的词云图片
#输出词云图片到文件
plt.savefig(r'.\static\assets\img\wordcloudshenyang.jpg',dpi=500)