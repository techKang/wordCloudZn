# -*- coding:utf-8 -*-

'''
This is main python file. Just run it!
'''
__author__ = 'Kangsir'

import splitChinese
import txt2words
import countFreq
import deleteSingleWord
import wordCloudGene


def run():
    runClass1 = splitChinese.SplitChinese()
    runClass1.splitChinese()
    runClass2 = txt2words.Txt2words(srcfile='splited.txt', desfile='des.txt', encoding='GB18030')
    runClass2.cntxt()
    runClass3 = countFreq.CountFreq(srcfile='des.txt', encoding='GB18030')
    runClass3.countFreq()
    runClass4 = deleteSingleWord.DeleteSingleWord(srcfile='freq.txt')
    runClass4.deleteSingleWord()
    runClass5 = wordCloudGene.WorldCloudGene(encoding='utf-8', maxword=1000)
    runClass5.worldCloudGene()


if __name__ == '__main__':
    run()
