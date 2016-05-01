# -*- coding: utf-8 -*-
"""
Created on Sun May  1 09:22:59 2016

@author: Moon
"""
import pandas as pd
import os, sys


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
    


test = loadInPd(history_list[0])