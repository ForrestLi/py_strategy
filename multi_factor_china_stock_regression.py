'''
Created on Oct 27, 2020

@author: Forrest Li
'''

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import chinastock as cs

db_connection_str = 'mysql+pymysql://root:A1234567@localhost/ms_financials_db'
db_connection = create_engine(db_connection_str)
pd.set_option("display.max_rows", None, "display.max_columns", None)

ticker_df = pd.read_sql("""
         SELECT * 
         FROM ms_financials_db.morningstar_key_eps_percent 
         where year_over_year>0 and 3_year_average>25 and 5_year_average>20 and 10_year_average>20 and period in ('2019-12-31','2020-03-31','2020-06-30','2020-09-30') order by 5_year_average desc        
         """
        , con=db_connection)

print(ticker_df)
multi_factor_df = pd.read_sql("""
         SELECT * 
         from ms_financials_db.morningstar_key_profitability 
         where ticker in 
         (SELECT ticker 
         FROM ms_financials_db.morningstar_key_eps_percent 
         where 3_year_average>25 and 5_year_average>20 and 10_year_average>10 and period in ('2019-12-31','2020-03-31','2020-06-30','2020-09-30') order by 5_year_average desc)
         """
         , con=db_connection)


print(multi_factor_df)
stock_ticker='001979'

stock_data_time_dic={i[0]:i[1] for i in cs.get_stock_history(code=stock_ticker,exchange='SZ')}

    
print(stock_data_time_dic)
    #print(stock_data_time_dic['20161230'])
#print(stock_data_time_dic)
stock_pd=pd.DataFrame.from_dict(stock_data_time_dic,columns=['Date','Price'],orient='index') 
#print(stock_pd['Price'].pct_change())
daily_pct_change=stock_pd.pct_change()
print(daily_pct_change)
#daily_pct_change=stock_pd.pct_change().resample('M')
#monthly_pct_ret=stock_pd.pct_change().resample('M').agg(lambda x:(x+1).prod -1)
#print(monthly_pct_ret)
#moving_average_20d=stock_pd.rolling(window=20).mean()

