# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:42:23 2015

目標是抓出日經的daily，並把他存成csv,同時寫入mySQL
"""
import urllib.request
import datetime
import json
import pandas as pd

d0 = datetime.datetime.now() #d0 是今天
d0 = d0.strftime("%Y-%m-%d_%H%M%S")
print(d0)
#print(d0) 已經掉定這個格式是到秒


file_path = 'C:/1save/taipei_parking/'

url = 'http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000292-002'
#print (url)

response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object
text = data.decode('utf-8')
text1 = json.loads(text)# a `str`; this step can't be used if data is binary
#text = text[13:] #第13個是位
#print(text1)

saveToCSV = text1['result']['records']

b4csv = pd.DataFrame(saveToCSV)
b4csv = b4csv[b4csv.AVAILABLECAR != '-9']
b4csv = pd.DataFrame.reset_index(b4csv)

aftcsv = pd.DataFrame.to_csv(b4csv)

#print(aftcsv)
csv_file = open(file_path + str(d0)+'.csv', 'w', encoding = 'utf-8' )

csv_file.write(aftcsv)

csv_file.close()

print ('The ' + str(d0) + ' is done')