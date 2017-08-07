# -*- coding:utf-8 -*-
'''
This python file is used to delete auxiliary words in freq.txt.
'''


class DeleteSingleWord():
    def __init__(self, srcfile='src.txt', desfile='notionFreq.txt', cutlen=50, enconding='utf-8'):
        self.srcfile = srcfile
        self.desfile = desfile
        self.cutlen = cutlen
        self.encoding = enconding

    def deleteSingleWord(self):
        with open(self.srcfile, 'r', encoding=self.encoding) as src:
            line = src.readline().split()
            i = 0
            output = ''
            while line != []:
                i += 1
                print(line)
                if len(line[0]) == 1 and i < self.cutlen:
                    line = src.readline().split()
                    continue
                output += str(line[0]) + '  ' + str(line[1]) + '\n'
                line = src.readline().split()
        with open(self.desfile, 'w',encoding='utf-8') as des:
            des.write(output)


if __name__ == "__main__":
    testClass = DeleteSingleWord(srcfile='freq.txt')
    testClass.deleteSingleWord()
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
