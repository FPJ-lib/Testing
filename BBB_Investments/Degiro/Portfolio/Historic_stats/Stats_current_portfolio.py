import pandas as pd
import pandas_datareader.data as web
import math
import matplotlib.pyplot as plt

start_date = '2020-06-1'

df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Degiro/Output_csv/port_current.csv')

'''
Objective:
---Get an Idea of Current Portfolio Performance in the Past:
---Plotting this year return


Optimize:
---#SHARES * Price Columns:
---Stats:


'''

print('\n')
print(df)
print('\n')

price = pd.DataFrame(columns=df['Ticker'])
portfolio = []

for ticker in df['Ticker']:
    print(ticker)
    price[ticker] = web.DataReader(ticker , 'yahoo', start = start_date)['Adj Close']
print('\n')

# Printing Number of columns 
#print('Number of columns :', price.shape[1])
#for i in range(price.shape[1]):
#    price[i] = price[i] * df['Quant.'].iloc[i]
#print(price.head(3))
#print(df['Quant.'].iloc[1])
#print(df.loc[df['Ticker'] == 'ALTR.LS']['Quant.'])
#for ticker in df['Ticker']:
#    price[ticker] = df.loc[df['Ticker'] == ticker]['Quant.'] * price[ticker]

price['ALTR.LS'] = price['ALTR.LS'] * 31
price['ITX.MC'] = price['ITX.MC'] * 8
price['JMT.LS'] = price['JMT.LS'] * 89
price['VID.MC'] = price['VID.MC'] * 3

print(price.head(3))

price['Portf'] = price['ALTR.LS'] + price['ITX.MC'] + price['JMT.LS'] + price['VID.MC']
print(price.tail(10))
price['Portf'] = price['Portf'].pct_change().dropna()

#STATS:
print('\nStats on Portfolio:')
mean = price['Portf'].mean()
std = price['Portf'].std()
IS = mean/std

print('\nMean:', round(mean*100 ,2),'%')
print('STD :', round(std*100 ,2),'%')
print('IS  :', round(IS ,2))

#Annual:
print('\nAnnual: \nMean: ', round(100*mean*360, 2) )
print('STS: ', round(std*math.sqrt(360)*100,2))

price['Portf'].cumsum().plot()
plt.show()

print('\nOver:')