#https://codingandfun.com/python-scraping-how-to-get-sp-500-companies-from-wikipedia/
import bs4 as bs
import requests
import pandas as pd
import numpy as np
print()

#ALL DATA:
'''INPUTS'''
ticker =[
    'EDP.LS',
    'EDPR.LS',
    'ALSS.LS1',
    'KO',
    'PEP.OQ'
]

#Webscrap
for ticker in ticker:
    link = 'https://www.reuters.com/companies/' + ticker +'/profile'
    resp = requests.get(link)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('div' , {'class': 'Profile-about-1d-H-'})
    df = table.find('p').text
    print()
    print(df)

print()
print('OVER:')