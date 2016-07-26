# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:00:21 2016

@author: g3094510
"""

import pandas as pd
import csv
import os, py
import numpy as np
import datetime


file_path = 'C:/1save/taipei_parking/' #檔案路徑的代號，這邊放歷史資料
history_list = []
justName = []
judgeW= []
dateTimeL = []

def insertColon(string = str, index = int):
    return string[:index] + ':' + string[index:]

for name in os.listdir(file_path):
    timeIn = name[:-4].replace("_", "T")
    timeIn = insertColon(timeIn, -4)
    timeIn = insertColon(timeIn, -2)
    justName.append(timeIn)  #這一步,只抓了名字的
    name = file_path + name
    history_list.append(name)
    
for eachName in justName:
    obj = datetime.datetime.strptime(eachName,'%Y-%m-%dT%H:%M:%S')
    dateTimeL.append(obj)

def weekendOrNot(path = str, yesNo = bool):
    tempL = []
    for each in os.listdir(path):
        tempL.append(each)
    

#target_list = weekendOrNot(file_path, True)
