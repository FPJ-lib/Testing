#https://codingandfun.com/python-scraping-how-to-get-sp-500-companies-from-wikipedia/
import bs4 as bs
import requests
import pandas as pd
import numpy as np
print('\n')

#ALL DATA:
#ticker ='VID.MC'
ticker ='JMT.LS'
statement = ['income-statement-', 'balance-sheet-', 'cash-flow-']
freq = ['annual', 'quarterly']

#Webscrap
link=[]
def get_reuters(ticker, statement=statement[0], freq = freq[1]):
    link = 'https://www.reuters.com/companies/' + ticker +'/financials/' + statement + freq
    resp = requests.get(link)
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table')

    col0 = []
    col1 = []
    col2 = []
    col3 = []
    col4 = []
    names =[]

    for row in table.findAll('tr')[1:]:
            ticker = row.findAll('td')[0].text
            company = row.findAll('td')[1].text
            sector = row.findAll('td')[2].text
            industry = row.findAll('td')[3].text
            column4 = row.findAll('td')[4].text
            
            name = row.find('span').text
            names.append(name)

            col0.append(ticker)
            col1.append(company)
            col2.append(sector)
            col3.append(industry)
            col4.append(column4)

    '''
    dates = []
    for row in table.findAll('tr')[0:1]:
        for i in range(1,6):
            #print(row)
            date = row.findAll('th')[i]
            dates.append(date)
            print()
            print(date)
        print('\n')
    '''
    
    #Clean Names:
    '''
    col0 = list(map(lambda s: s.strip(), col0))
    col1 = list(map(lambda s: s.strip(), col1))
    col2 = list(map(lambda s: s.strip(), col2))
    col3 = list(map(lambda s: s.strip(), col3))
    col4 = list(map(lambda s: s.strip(), col4))
    '''

    #DataFrame Concat:
    names = pd.DataFrame(names,columns=['Account'])
    col0 = pd.DataFrame(col0,columns=['Date -0'])
    col1 = pd.DataFrame(col1, columns=['Date -1']) 
    col2 = pd.DataFrame(col2, columns=['Date -2'])
    col3 = pd.DataFrame(col3,columns=['Date -3'])
    col4 = pd.DataFrame(col4,columns=['Date -4'])

    #Full Table from Wiki:
    df = pd.concat([names,col0,col1 ,col2, col3, col4], axis=1) #.reindex(columns=[tickerdf.index])
    df = df.reindex(col0.index)
    print('\n')
    return df, link


df , link = get_reuters(ticker, statement=statement[0], freq=freq[0]) 

print(df)

#Save CSV:
path_csv ='/Users/filipepessoajorge/OneDrive/X02 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/WebScrapping/Financials_Statements/Firms_df/%s.csv' % ticker
df.to_csv(path_csv, index=False)

print('\nCheck Values & Dates:\n',link)
print('\nOVER:')