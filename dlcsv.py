# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:42:23 2015

目標是抓出日經的daily，並把他存成csv,同時寫入mySQL
"""
import urllib.request
import datetime
import re
import json
import pandas as pd
d0 = datetime.datetime.now() #d0 是今天
d0 = d0.strftime("%Y-%m-%d_%H%M%S")
print(d0)
#print(d0) 已經掉定這個格式是到秒


local_path = 'C:/1save/taipei_parking/'


url = 'http://shiaobin.com/csv/'
#print (url)



response = urllib.request.urlopen(url)
data = response.read()      # a `bytes` object

text = data.decode('utf-8')
#print(text)
name_list = []
dl_list = []

dl_link = re.findall('\"\d{4}.*\.csv\"',text)
for i in dl_link:
    i = i[1:-1]
    name_list.append(i)
    i = url + i
    dl_list.append(i)
print(dl_list)

for csv_url in dl_list:
    
    csv_file = urllib.request.urlopen(csv_url)
    b4save = csv_file.read()
    b4save = b4save.decode('utf-8')
    with open(local_path + csv_url[-21:],'w', encoding = 'utf-8') as files:
        files.write(b4save)
        
    

"""
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

"""