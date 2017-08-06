# -*- coding:utf-8 -*-
import re
'''
this python file is used to remove all punctuations in source txt files.
'''

class Txt2words():
    def __init__(self,srcfile='src.txt',desfile='des.txt'):
        self.srcfile=srcfile
        self.desfile=desfile

    def entxt(self):
        srcname = self.srcfile
        desname = self.desfile
        with open(srcname, 'r') as src:
            srctext = src.read()
            with open(desname, 'w') as des:
                destext = re.sub('\W\D',' ',srctext)
                des.write(destext)
                pass
            pass
        pass


if __name__=='__main__':
    testClass=Txt2words()
    testClass.entxt()
    with open(testClass.srcfile,'r') as src:
        print('source file:')
        srctext=src.read(100)
        print(srctext)
        pass
    with open(testClass.desfile,'r') as des:
        print('destination file:')
        destext=des.read(100)
        print(destext)
        pass


