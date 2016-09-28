# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:55:20 2016


"""
import pandas as pd
import math

filePath = 'C:/1save/'

fileN = 'weekend.csv'

raw = pd.read_csv(filePath + fileN, index_col = 0)

fileNinfo ='information.csv'
info = pd.read_csv(filePath + fileNinfo)

rawIn = [x for x in raw.index]

#print(rawIn[:10])

infoColN = [x for x in info.columns.values]
infoColN[0] = "id"

#raw = pd.set_index([[0]])

infoDF = pd.DataFrame(index=raw.index)

#infoDF = infoDF.join(info, how = "inner")
raw = raw.T #先把他反轉, 因為 Index 用時間比較好, 這樣你只要用
#test = raw["10022"]

test = raw[10022]

count = test.count()

nanCount = test.isnull().sum()
