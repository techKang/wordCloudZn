# -*- coding:utf-8 -*-
import re

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码

'''
this python file is used to remove all punctuations in source txt files.
'''


class Txt2words():
    def __init__(self, srcfile='src.txt', desfile='des.txt',encoding='utf-8'):
        self.srcfile = srcfile
        self.desfile = desfile
        self.encoding=encoding

    def entxt(self):
        srcname = self.srcfile
        desname = self.desfile
        with open(srcname, 'r', encoding=self.encoding) as src:
            srctext = src.read()
        with open(desname, 'w') as des:
            destext = re.sub('\W', ' ', srctext)
            destext = ' '.join(destext.split())
            des.write(destext)
            pass
        pass

    def cntxt(self):
        srcname = self.srcfile
        desname = self.desfile
        with open(srcname, 'r',encoding=self.encoding) as src:
            srctext = src.read()
        with open(desname, 'w',encoding='GB18030') as des:
            destext = re.sub('[，。？！《》（）,.?!"\'“”‘’：、…\[\]；· ─□0-9a-zA-Z]', ' ', srctext)
            destext = ' '.join(destext.split())
            des.write(destext)
            pass
        pass


if __name__ == '__main__':
    testClass = Txt2words(srcfile='splited.txt', desfile='des.txt',encoding='GB18030')
    testClass.cntxt()
    with open(testClass.srcfile, 'r', encoding=testClass.encoding) as src:
        print('source file:')
        srctext = src.read(300)
        print(srctext)
        pass
    with open(testClass.desfile, 'r') as des:
        print('\ndestination file:')
        destext = des.read(300)
        print(destext)
        pass
