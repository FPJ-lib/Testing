import pandas as pd 
import pandas_datareader.data as web
import math

start_date = '2004-12-31'

psi20 = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/PSI20/Output_csv/psi20.csv')
print(psi20)

#Table with Prices:
price = pd.DataFrame(columns=psi20['ticker'])
print('\n')

total_ret = []

#Fetch Data
for ticker in psi20['ticker']:
    print(ticker)
    price[ticker] = web.DataReader(ticker , 'yahoo', start=start_date)['Adj Close']
    total_ret.append(price[ticker][-1]/price[ticker][0] - 1)

#price['PSI20.LS'] = web.DataReader('PSI20.LS' , 'yahoo', start=start_date)['Adj Close']

price.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/PSI20/Output_csv/psi20_prices.csv.csv')

print(price)

price = price.pct_change()
price.dropna(inplace=True)

print(price)

'''

av_return = []
av_std = []
for ticker in psi20['ticker']:
    print(ticker)
    av_return.append(price[ticker].mean())
    av_std.append(price[ticker].std())

print('\n')
psi20['ret'] = av_return
psi20['ret'] = round( psi20['ret'] *100 * 360 , 2 )

psi20['std'] = av_std
psi20['std'] = round( psi20['std'] * math.sqrt(360) * 100 , 2)

psi20['IS'] = round(psi20['ret']/psi20['std'],2)

psi20['Total_Ret'] = total_ret
psi20['Total_Ret'] = round( psi20['Total_Ret'] *100 , 2 )

psi20 = psi20.sort_values(by=['Total_Ret'], ascending = False)
print(psi20, '\nStart Date: \n%s' % start_date)

#Save for CSV:
#psi20.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/PSI20/Output_csv/psi20_ret.csv')


print('')
'''