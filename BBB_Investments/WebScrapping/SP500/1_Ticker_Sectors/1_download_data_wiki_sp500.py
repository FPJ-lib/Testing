#https://codingandfun.com/python-scraping-how-to-get-sp-500-companies-from-wikipedia/
import bs4 as bs
import requests
import pandas as pd
import numpy as np

print('\n')

#ALL DATA:
resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})



tickers = []
companies = []
sectors = []
industries = []

for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        company = row.findAll('td')[1].text
        sector = row.findAll('td')[3].text
        industry = row.findAll('td')[4].text
        
        tickers.append(ticker)
        companies.append(company)
        sectors.append(sector)
        industries.append(industry)

#Clean Names:
tickers = list(map(lambda s: s.strip(), tickers))
companies = list(map(lambda s: s.strip(), companies))
sectors = list(map(lambda s: s.strip(), sectors))
industries = list(map(lambda s: s.strip(), industries))

#DataFrame Concat:
tickerdf = pd.DataFrame(tickers,columns=['ticker'])
companydf = pd.DataFrame(companies, columns=['company']) 
sectordf = pd.DataFrame(sectors, columns=['sector'])
industrydf = pd.DataFrame(industries,columns=['industry'])

#Full Table from Wiki:
df = pd.concat([tickerdf,companydf ,sectordf, industrydf], axis=1, join_axes=[tickerdf.index]) #.reindex(columns=[tickerdf.index])

#Save CSV:
df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv', index=False)


#print(df)