# -*- coding:utf-8 -*-
'''
splitChinese.py
~~~~~~~~~~~~~~~~~
This python file is used to split Chinese sentences to separated words.
Source file should be processed by txt2words.py after be processed by this python file.
'''

import jieba


class SplitChinese():
    def __init__(self, srcfile='src.txt', desfile='splited.txt'):
        self.srcfile = srcfile
        self.desfile = desfile

    def splitChinese(self):
        with open(self.srcfile, 'r', encoding='utf-8') as src:
            geneStr = jieba.cut(src.read())
            destext = " ".join(geneStr)
            pass
        with open(self.desfile, 'w') as des:
            des.write(destext.encode('utf-8').decode('utf-8'))
            pass


if __name__ == '__main__':
    testClass = SplitChinese()
    testClass.splitChinese()
    with open(testClass.srcfile, 'r', encoding='utf-8') as src:
        print('source file:')
        srctext = src.read(300)
        print(srctext)
        pass
    with open(testClass.desfile, 'r') as des:
        print('\ndestination file:')
        destext = des.read(300)
        print(destext)
        pass
