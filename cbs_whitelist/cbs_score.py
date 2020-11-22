'''
Created on Nov 14, 2020

@author: Forrest Li
'''
import requests
from lxml import html
import requests

def get_cbs_score(ticker):
    if not isinstance(ticker, str):
        ticker=str(ticker)
    #URL = 'https://caibaoshuo.com/companies/'+ticker+'#annualCbsChartModal'
    URL = 'https://caibaoshuo.com/companies/'+ticker
    user_agent=r'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; LCTE; rv:11.0) like Gecko'
    headers={'User-Agent':user_agent}
    response = requests.get(url=URL, params=None)
    scode=response.status_code
    if (scode==200):
       tree = html.fromstring(response.content)
       #cbs_score=tree.xpath('//span[@class="blurred span_l"]/text()')
       #print(tree)
       #cbs_score=tree.xpath('//a[@data-target="#annualCbsChartModal"]/text()')
       #cbs_score=tree.xpath('//a[@data-toggle="modal"]/text()')       
       #return(cbs_score)
       cbs_score_a=tree.xpath('//a[@data-toggle="modal"]/text()')      
       cbs_score_b=tree.xpath('//span[@class="blurred span_l"]/text()')
       return(cbs_score_a,cbs_score_b)
    else:
       return('NAN')
   
score= get_cbs_score('000048')
print(score)  

