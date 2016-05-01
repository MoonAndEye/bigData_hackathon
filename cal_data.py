# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:22:59 2016

@author: Moon
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os, sys
import csv

plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

merge_base = ['available' , 'id', 'time']#這個放要合併基準

file_path = 'C:/1save/taipei_parking/' #檔案路徑的代號，這邊放歷史資料
history_list = []
for name in os.listdir(file_path):
    name = file_path + name
    history_list.append(name)
    

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
    
#test = loadInPd(history_list[0])

result_df = loadInPd(history_list[0])
result_df = result_df.set_index('id')
result_df = result_df.drop(['available','time'], axis = 1)

csv_path = "C:/1save/parking_test2.csv"

plat_df = pd.read_csv(csv_path)
#test = pd.DataFrame(loadInPd(history_list[0]))

def addData(out, add_list):
    temp = pd.DataFrame(loadInPd(add_list))
    time_index = add_list[-21:-4]
    temp = temp.set_index('id')
    out[time_index] = temp['available']
    return(out)
"""
test = addData(result_df,history_list[0])
test2 = pd.DataFrame(loadInPd(history_list[0]))

"""
for all_csv in history_list:
    result_df = addData(result_df, all_csv)    



