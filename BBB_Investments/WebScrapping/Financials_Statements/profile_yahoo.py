#https://codingandfun.com/python-scraping-how-to-get-sp-500-companies-from-wikipedia/
import bs4 as bs
import requests
import pandas as pd
import numpy as np
print()

loop = 1
psi20 = 1

#ALL DATA:
'''INPUTS'''
ticker =[
    'EDP.LS',
    'EDPR.LS',
    'ALSS.LS1',
    'KO',
    'PEP.OQ'
]

if psi20 ==1:
    psi20 = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/PSI20/Output_csv/psi20.csv')
    print(psi20)
    ticker = psi20['ticker'].to_list()
else:
    sp500 = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv')
    print(sp500.head(3))
    ticker = sp500['ticker'].to_list()

print()

#Webscrap
profiles = []
for ticker in ticker[:50]:
    link = 'https://finance.yahoo.com/quote/'+ticker+'/profile?p='+ticker
    resp = requests.get(link)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('section' , {'class': 'quote-sub-section Mt(30px)'})
    
    txt_profile = table.find('p').text
    profiles.append(txt_profile)
    print(ticker)

for i in profiles:
    print('\n',ticker,':\n',i)

print()
print('OVER:')