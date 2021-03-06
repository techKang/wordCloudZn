# -*- coding:utf-8 -*-
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


class WorldCloudGene():
    def __init__(self, picture='testim.png', srcfile='notionFreq.txt', encoding='utf-8', maxword=2000,fontsize=100):
        self.picture = picture
        self.srcfile = srcfile
        self.encoding = encoding
        self.maxword = maxword
        self.fontsize=fontsize

    def worldCloudGene(self):
        # 获取当前文件路径
        # __file__ 为当前文件, 在ide中运行此行会报错,可改为
        # d = path.dirname('.')
        d = path.dirname(__file__)

        # 读取文本 alice.txt 在包文件的example目录下
        # 内容为
        """
        Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll

        This eBook is for the use of anyone anywhere at no cost and with
        almost no restrictions whatsoever.  You may copy it, give it away or
        re-use it under the terms of the Project Gutenberg License included
        with this eBook or online at www.gutenberg.org
        """
        txt_freq = {}
        with open(path.join(d, self.srcfile), 'r', encoding=self.encoding) as src:
            line = src.readline().split()
            i = 0
            while i < self.maxword or line == []:
                txt_freq.update({line[0]: int(line[1])})
                line = src.readline().split()
                i += 1
        # print(txt_freq)

        # text = open(path.join(d, 'alice.txt'), encoding='utf-8').read()

        # read the mask / color image
        # taken from http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
        # 设置背景图片
        alice_coloring = imread(path.join(d, self.picture))

        wc = WordCloud(background_color="white",  # 背景颜色max_words=2000,# 词云显示的最大词数
                       mask=alice_coloring,  # 设置背景图片
                       stopwords=STOPWORDS.add("said"),
                       max_words=self.maxword,
                       max_font_size=300,  # 字体最大值
                       font_path=path.join(d, 'msyh.ttf'),
                       random_state=42)
        # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
        # wc.generate(text)
        wc.generate_from_frequencies(txt_freq)
        # txt_freq例子为[('词a', 100),('词b', 90),('词c', 80)]
        # 从背景图片生成颜色值
        image_colors = ImageColorGenerator(alice_coloring)

        # 以下代码显示图片
        plt.imshow(wc)
        plt.axis("off")
        # 绘制词云
        plt.figure()
        # recolor wordcloud and show
        # we could also give color_func=image_colors directly in the constructor
        plt.imshow(wc.recolor(color_func=image_colors))
        plt.axis("off")
        # 绘制背景图片为颜色的图片
        plt.figure()
        plt.imshow(alice_coloring, cmap=plt.cm.gray)
        plt.axis("off")
        plt.show()
        # 保存图片
        wc.to_file(path.join(d, "result.png"))


if __name__ == "__main__":
    testClass = WorldCloudGene(encoding='GB18030')
    testClass.worldCloudGene()
