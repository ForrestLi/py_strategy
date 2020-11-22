from sqlalchemy import create_engine
import pymysql
import pandas as pd
import chinastock as cs

db_connection_str = 'mysql+pymysql://root:A1234567@localhost/ms_financials_db'
db_connection = create_engine(db_connection_str)

pd.set_option("display.max_rows", None, "display.max_columns", None)
ticker_df = pd.read_sql(
         """
         SELECT * FROM ms_financials_db.morningstar_key_eps_percent where 3_year_average>25 and 5_year_average>20 and 10_year_average>10 and period in ('2019-12-31','2020-03-31','2020-06-30','2020-09-30')
         order by 3_year_average desc
         """
         , con=db_connection)

print(ticker_df)
multiple_factor_df = pd.read_sql("""
         SELECT * 
         from ms_financials_db.morningstar_key_profitability 
         where ticker in 
         (SELECT ticker FROM ms_financials_db.morningstar_key_eps_percent where 3_year_average>25 and 5_year_average>20 and 10_year_average>10 and period='2019-12-31')
         limit 100
         """
         , con=db_connection)

#print(df.groupby(['ticker'])['return_on_equity_percent'].mean())
#print(multiple_factor_df)

#adj_price_history = cs.get_stock_history_adj(code='000048',exchange='SS')
#print(adj_price_history)

