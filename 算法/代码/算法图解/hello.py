#GowRptWordCloudV1.py
import jieba
import wordcloud
from scipy.misc import imread
mask = imread("C:\\Users\\stormmao\\Desktop\\wujiao.png")
f = open("C:\\Users\\stormmao\\Desktop\\一号文件.txt","r",encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(\
    width = 1000, height = 700,\
    background_color = "white",
    font_path = "msyh.ttc", mask = mask
    )
w.generate(txt)
w.to_file("grwordcloud.png")