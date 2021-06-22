#https://codingandfun.com/python-scraping-how-to-get-sp-500-companies-from-wikipedia/
import bs4 as bs
import requests
import pandas as pd
import numpy as np

print('\n')

#ALL DATA:
resp = requests.get('https://en.wikipedia.org/wiki/PSI-20')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable', 'style':'text-align: center;'})

#print(table)

companies = []
sectors = []
tickers = []

for row in table.findAll('tr'):
        company = row.findAll('td')[0].text
        sector = row.findAll('td')[1].text
        ticker = row.findAll('td')[2].text + '.LS'
        
        companies.append(company)
        sectors.append(sector)
        tickers.append(ticker)

#Clean Names:
companies = list(map(lambda s: s.strip(), companies))
sectors = list(map(lambda s: s.strip(), sectors))
tickers = list(map(lambda s: s.strip(), tickers))

#DataFrame Concat:
companydf = pd.DataFrame(companies, columns=['company']) 
sectordf = pd.DataFrame(sectors, columns=['sector'])
tickerdf = pd.DataFrame(tickers ,columns=['ticker'])

#Full Table from Wiki:
df = pd.concat([tickerdf,companydf ,sectordf], axis=1, join_axes=[tickerdf.index]) #.reindex(columns=[tickerdf.index])
print('\n')

print(df)

#Save CSV:
df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/PSI20/Output_csv/psi20.csv', index=False)

print('\n')