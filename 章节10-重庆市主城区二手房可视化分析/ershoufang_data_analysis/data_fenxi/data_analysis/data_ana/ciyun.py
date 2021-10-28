# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import jieba
from imageio import imread
"""重庆主城区二手房数据词云"""
#基础配置数据
filename = "../data_file/new_new_utf_8.csv"
backpicture = "../resources/house2.jpg"
savepicture = "./picture/重庆二手房数据词云2.png"
fontpath = "../resources/simhei.ttf"
stopwords = ["null","暂无","数据"]
#读入数据文件
comment_text = open(filename,encoding="utf-8").read()  
# 读取背景图片
color_mask = imread(backpicture)
#结巴分词,同时剔除掉不需要的词汇    
ershoufang_words = jieba.cut(comment_text)
ershoufang_words = [word for word in ershoufang_words if word not in stopwords]
cut_text = " ".join(ershoufang_words)
#设置词云格式
cloud = WordCloud(
    #设置字体，不指定就会出现乱码
    font_path=fontpath,
    #设置背景色
    background_color='white',
    #词云形状
    mask=color_mask,
    #允许最大词汇
    max_words=2000,
    #最大号字体
    max_font_size=60
   )
# 产生词云
word_cloud = cloud.generate(cut_text) 
#保存图片
word_cloud.to_file(savepicture) 