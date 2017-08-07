# -*- coding:utf-8 -*-

'''
This is main python file. This is used to analysis QQ charting records or any files.
Before start, you should install wordCloud, anaconda3.
'''
__author__ = 'Kangsir'

import qqHistory
import splitChinese
import txt2words
import countFreq
import deleteSingleWord
import wordCloudGene


def run():
    runClass0=qqHistory.QqHistory(srcfile='history.txt',desfile='src.txt')
    runClass0.qqHistroy()
    runClass1 = splitChinese.SplitChinese()
    runClass1.splitChinese()
    runClass2 = txt2words.Txt2words(srcfile='splited.txt', desfile='des.txt', encoding='GB18030')
    runClass2.cntxt()
    runClass3 = countFreq.CountFreq(srcfile='des.txt', encoding='GB18030')
    runClass3.countFreq()
    runClass4 = deleteSingleWord.DeleteSingleWord(srcfile='freq.txt')
    runClass4.deleteSingleWord()
    runClass5 = wordCloudGene.WorldCloudGene(encoding='utf-8', maxword=300,fontsize=200)
    runClass5.worldCloudGene()


if __name__ == '__main__':
    run()
