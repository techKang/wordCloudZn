# -*- coding:utf-8 -*-
import re

class QqHistory():
    def __init__(self, srcfile='src.txt', desfile='des.txt', enconding='utf-8'):
        self.srcfile = srcfile
        self.desfile = desfile
        self.encoding = enconding

    def qqHistroy(self):
        with open(self.srcfile,'r',encoding=self.encoding) as src:
            line=src.readline()
            output=''
            while line!='':
                if not re.match('201[67]\-\d{2}\-\d{2}', line):
                    output+=line
                line=src.readline()
                output=output.replace('[图片]','')
                output = output.replace('[表情]', '')
        with open(self.desfile,'w',encoding='utf-8') as des:
            des.write(output)


if __name__ == "__main__":
    testClass = QqHistory()
    testClass.qqHistroy()
    with open(testClass.srcfile, 'r', encoding=testClass.encoding) as src:
        print('source file:')
        srctext = src.read(300)
        print(srctext)
        pass
    with open(testClass.desfile, 'r', encoding='utf-8') as des:
        print('\ndestination file:')
        destext = des.read(600)
        print(destext)
        pass