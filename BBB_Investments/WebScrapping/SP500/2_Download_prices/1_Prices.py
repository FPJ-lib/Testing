import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start_date='2010-01-01'

df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv')
df['ticker'] = df['ticker'].str.replace(".", "-")

#Create Arrays
price = pd.DataFrame(columns=df['ticker'])

#Waiting %
size = df['ticker'].size
i=0

#Fetch Data
for ticker in df['ticker']:
    i+=1
    print(int(100* i/size), '% ,', ticker )
    price[ticker] = web.DataReader(ticker , 'yahoo', start=start_date)['Adj Close']
    #print(price[ticker])
print(price)

price.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/Prices_SP500_2010/df.csv', index= False)