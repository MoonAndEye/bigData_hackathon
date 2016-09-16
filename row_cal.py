# -*- coding: utf-8 -*-
"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question

In [11]: df = pd.DataFrame([[1., 2.], [3., 4.]], columns=['A', 'B'])

In [12]: df2 = pd.DataFrame([[5., 10.]], columns=['A', 'B'])

In [13]: df.div(df2)
Out[13]: 
     A    B
0  0.2  0.2
1  NaN  NaN

In [14]: df.div(df2.iloc[0])
Out[14]: 
     A    B
0  0.2  0.2
1  0.6  0.4

df1.div(df2.ix[0],axis='columns')

http://stackoverflow.com/questions/22642162/python-divide-each-row-of-a-dataframe-by-another-dataframe-vector
"""

import pandas as pd

a = pd.DataFrame([[1., 2.], [3., 4.]])

b = pd.DataFrame([[0.5], [0.25]])

c = a/b.values[0,:]
