# -*- coding:utf-8 -*-
'''
this python file is used to count word frequency in source text and print it to freq.txt
'''


class CountFreq():
    def __init__(self, srcfile='src.txt', desfile='freq.txt'):
        self.srcfile = srcfile
        self.desfile = desfile

    def countFreq(self):
        with open(self.srcfile, 'r', encoding='utf-8') as src:
            words = src.read().split()
            pass
        words_index = set(words)
        counts_dict = {index: words.count(index) for index in words_index}
        output = ''
        for word in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
            output += str(word) + '  ' + str(counts_dict[word]) + '\n'

        # print(output)
        with open(self.desfile, 'w', encoding='utf-8') as des:
            des.write(output)
            pass


if __name__ == "__main__":
    testClass = CountFreq(srcfile='des.txt')
    testClass.countFreq()
    with open(testClass.srcfile, 'r', encoding='utf-8') as src:
        print('source file:')
        srctext = src.read(300)
        print(srctext)
        pass
    with open(testClass.desfile, 'r', encoding='utf-8') as des:
        print('\ndestination file:')
        destext = des.read(600)
        print(destext)
        pass
