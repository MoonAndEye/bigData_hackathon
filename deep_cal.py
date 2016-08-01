# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:55:20 2016


"""
import pandas as pd


filePath = 'C:/1save/'

fileN = 'weekend.csv'

raw = pd.read_csv(filePath + fileN, index_col = 0)

fileNinfo ='information.csv'
info = pd.read_csv(filePath + fileNinfo)

rawIn = [x for x in raw.index]

#print(rawIn[:10])

infoColN = [x for x in info.columns.values]
infoColN[0] = "id"

raw = pd.set_index([[0]])

infoDF = pd.DataFrame(index=raw.index)

#infoDF = infoDF.join(info, how = "inner")
