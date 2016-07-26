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
from datetime import date


file_path = 'C:/1save/taipei_parking/' #檔案路徑的代號，這邊放歷史資料
history_list = []
justName = []
#judgeW= []
dateTimeL = []

weekEndFL = []
weekDayFL = []

weekEndNL = []
weekDayNL = []

def insertColon(string = str, index = int):
    """
    在原始字串的某個位置,插入冒號.
    第一變數放目標字串
    第二變數放要插入的位置
    """
    return string[:index] + ':' + string[index:]

for name in os.listdir(file_path):
    """
    掃過所有 file_path 內的檔名.
    把時間從 str轉成 datetime後,存入dateTimeL
    然後把檔案位置存入 history_list
    """
    timeIn = name[:-4].replace("_", "T")
    timeIn = insertColon(timeIn, -4)
    timeIn = insertColon(timeIn, -2)
    obj = datetime.datetime.strptime(timeIn,'%Y-%m-%dT%H:%M:%S')
    dateTimeL.append(obj) #obj 是轉換成 datetime後的東西
    #print(obj.isoweekday())
    
    if obj.isoweekday() == 6:
        weekEndFL.append(file_path + name)
        weekEndNL.append(obj)
    elif obj.isoweekday() == 7:
        weekEndFL.append(file_path + name)
        weekEndNL.append(obj)
    
    else:
        weekDayFL.append(file_path + name)
        weekDayNL.append(obj)
    
    justName.append(timeIn)  #這一步,只抓了名字的檔案,以後可能有用
    name = file_path + name
    history_list.append(name)
    
#print(dateTimeL[1000].isoweekday())
"""
#以下不需要了,我合併進 for loop
for each in dateTimeL:
    fileIn = dateTimeL.index(each)
    if each.isoweekday() == 6:
        weekEndNL.append(each)
        weekEndFL.append(history_list[fileIn])
    elif each.isoweekday() == 7:
        weekEndNL.append(each)
        weekEndFL.append(history_list[fileIn])
    else:
        weekDayNL.append(each)
        weekDayFL.append(history_list[fileIn])
"""        
        
"""
def weekendOrNot(path = str, yesNo = bool):
    tempL = []
    for each in os.listdir(path):
        tempL.append(each)
""" 

#target_list = weekendOrNot(file_path, True)
