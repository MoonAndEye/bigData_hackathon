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
#import time


#start_time = time.time() #這個是抓計算時間的

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
    
    """
    用 date.isoweekday() 判斷是否 Sat, Sun
    如果是,則把他放到 weekEnd
    否, 則放到 weekDay
    """
    
    
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

"""
#下面開始 分別把 weekday, weekend 的資料合成一個 DataFrame
#然後再分別輸出成 csv, 之後用另一個檔案直接計算 csv,而非每次都讀檔
"""

"""
#這個是舊的,如果新的成功了,就可以砍了
def loadInPd(_path):
    time = _path[-21:-4]
    pre_array =pd.read_csv(_path, skiprows = 1,encoding = 'utf-8')
    csv_columns = ['no-need1','no-need2','available','id']
    pre_array.columns = csv_columns
    pre_array = pre_array.drop(['no-need1', 'no-need2'], axis = 1)
    pre_array['time'] = time
    pre_array['time'] = pre_array['time'].astype(str)
    pre_array['available'] = pre_array['available'].astype(int)
    return(pre_array)
"""

def loadInPd(_path):
    pre_array = pd.read_csv(_path,index_col = [0])
    if pre_array["ID"][0] == pre_array["ID"][1]:
        pre_array = pre_array[1:]
    pre_array = pre_array.set_index("ID")
    pre_array = pre_array.drop("index", 1) #小的不要
    
    return (pre_array)


firstPD = pd.read_csv(history_list[0],index_col = [0]) #用index_col才不會一直有Unnamed
if firstPD["ID"][0] == firstPD["ID"][1]:
    firstPD = firstPD[1:]
"""
#不知道為什麼,第一行會重複,這個動作就是把他砍了,用if 判斷,一樣才砍
"""
columnL = list(firstPD.columns.values) #columnL 就是DataFrame的list 列表
indexL = firstPD[columnL[-1]] #indexL 則是放所有的停車場的 ID, 之後的合併標準

weekEndResult = pd.DataFrame(index = indexL) #先做出模版, index 用停車場ID

#preDF = loadInPd(weekEndFL[5000])

a1 = loadInPd(weekEndFL[0])
a1.columns = [weekEndNL[0]]
a2 = loadInPd(weekEndFL[1])
a2.columns = [weekEndNL[1]]
#a2.columns = a1[weekEndNL[1]]
a900 = loadInPd(weekEndFL[900])
a900.columns = [weekEndNL[900]]

weekEndResult = weekEndResult.join(a1, how = "outer")
weekEndResult = weekEndResult.join(a2, how = "outer")
weekEndResult = weekEndResult.join(a900, how = "outer")
"""
for each_raw in weekEndFL[:585]:
    preDF = loadInPd(each_raw)
    indexCount = weekEndFL.index(each_raw)
    dateIn = weekEndNL[indexCount]
    delList = []
    preIn = list(preDF.index.values)
    
    #colN = preDF.columns.values
    
    preDF.columns = [dateIn]
    #preDF = preDF.rename(columns = {"AVAILABLECAR", dateIn}) #這行有錯
    #delayMatrix = pd.concat([delayMatrix, b4_input], axis=1, join_axes=[b4_input.index])
    # result = pd.merge(left, right, left_index=True, right_index=True, how='outer')
    #weekEndResult = pd.concat([weekEndResult, preDF], axis = 1, join_axes=[weekEndResult.index], join = "outer")
    #weekEndResult = pd.merge(weekEndResult, preDF)
    #b4 = weekEndResult.copy()
    #weekEndResult = weekEndResult.join(preDF)
    #b4 = weekEndResult.copy()
    weekEndResult = pd.concat([weekEndResult, preDF], axis = 1, join_axes=[weekEndResult.index])
"""
#a = weekEndResult.index.values

#weekEndResult = firstPD.copy()
#weekEndResult = weekEndResult.set_index(columnL[-1])
#tempCol = list(weekEndResult.columns.values)

#for eachRaw in weekDayFL:
    





"""
#以下三行確定可以 run, 但先稍微優化一下
result_df = loadInPd(history_list[0])
result_df = result_df.set_index('id')
result_df = result_df.drop(['available','time'], axis = 1)
"""

#print("Run time --- %s seconds ---" % (time.time() - start_time))
#target_list = weekendOrNot(file_path, True)
