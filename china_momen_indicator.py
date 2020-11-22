'''
Created on Nov 3, 2020

@author: Forrest Li
'''

import pandas_datareader.data as reader
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta
import chinastock as cs

stock_ticker='001979'

def dateStringConverter(date_string):
    year = int(date_string[0:4])
    month = int(date_string[4:6])
    day = int(date_string[6:8])
    return dt.datetime(year, month, day)

stock_data_time_dic={dateStringConverter(i[0]):i[1] for i in cs.get_stock_history(code=stock_ticker,exchange='SZ')}

    
print(stock_data_time_dic)

china_pd=pd.Series(stock_data_time_dic).to_frame() 
daily_return=china_pd.pct_change()
print(daily_return)
monthly_return=daily_return.resample('M').agg(lambda x:(x+1).prod()-1)
print(monthly_return)