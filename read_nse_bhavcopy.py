# -*- coding: utf-8 -*-
"""

Read NSE daily bhavcopy file and display top 5 trading stocks
To increase performance read only SYMBOL, CLOSE & TOTTRDQTY columns only from csv file
"""
print("testing python")
import pandas as pd
print(pd.__version__)

data=pd.read_csv("/home/dataanalyst/data/nse/equity/bhavcopy/2018_10/cm11OCT2018bhav.csv",
                 usecols =('SYMBOL','CLOSE','TOTTRDQTY'))

print(type(data))
data1=data.sort_values(by=['TOTTRDQTY'], ascending = False)
print(data1.head(5))
