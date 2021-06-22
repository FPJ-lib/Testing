import pandas as pd
import pandas_datareader.data as web

start_date = '2020-10-01'

#Ticker From Yahoo.Finance
tickers = ['ALTR.LS','ITX.MC', 'JMT.LS' , 'VID.MC']
'''
Missing:
Do Tickers Prices with Merges after Downloading All Prices:

COSTS OF TRANSACTIONS of STOCK EXCHANGE:
As External:

'''
#import CSV DAta
portfolio_cost = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Degiro/Output_csv/portfolio_cost.csv')
portfolio_cost.rename(inplace=True, columns={'Quantidade':'Quant.', 'Valor':'Custo'})
#print(portfolio_cost)
dividends = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Degiro/Output_csv/Dividends_and_Tax.csv')
dividends = dividends.groupby(['Produto']).sum()
print(dividends)

#ADD STOCK RIGHTS: 13$ --> How much is it worth.
dividends = dividends.T
dividends['VIDRALA'] = dividends['VIDRALA'] + 13. 
dividends['INDITEX'] = dividends['INDITEX'] + 2.27 
dividends = dividends.T
print(dividends)

#Create Arrays
price = pd.DataFrame(columns=tickers)
mkt_price = []

print()

#Fetch Data
for ticker in tickers:
    print(ticker)
    price[ticker] = web.DataReader(ticker , 'yahoo')['Adj Close']
    mkt_price.append(round(price[ticker].iloc[-1],3))

#import Data from Portfolio:
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Degiro/Portfolio/Portfolio.csv')
df.drop(inplace= True, columns=['Valor', 'Ticker / ISIN','Valor em EUR'])
df['Preço'] = mkt_price
df['Valor'] = round(df['Quant.']*df['Preço'],2)
df['Ticker'] = tickers
#print(df)

#MERGE -- COST & Value:
df2 = df.merge(portfolio_cost, on = ['Produto','Quant.'], how='inner')
df2.drop(inplace=True, columns=[ 'Custo', 'Taxa'])

#Returns 
#df2['Even'] = -round(df2['Total']/df2['Quant.'],3)
df2['Ret'] = df2['Valor'] + df2['Total']
df2['Ret,%'] = round(100*df2['Ret']/-df2['Total'],2)

#Weight in Portfolio
sum_port = - df2['Total'].sum()
sum_port2 = - df2['Valor'].sum()
df2['Weight'] = round(-100*df2['Total']/sum_port,2)
df2['W_now'] = round(-100*df2['Valor']/sum_port2,2)

#WEIGHTED RETURN
ret_cap = (0.01 * df2['Weight']*df2['Ret,%']).sum()
#print('\nReturn w/o Dividends:\n', round(ret_cap,2),'%')

print('\n',df2,'\n')

# RETURNS - Confirming
ret = df2['Ret'].sum()
port = -df2['Total'].sum()
print('Ret:           ', round(ret,2))
print('Ret w/ div:    ', round(ret+ float(dividends.sum()),2))
print('Port:          ', round(port,2))
print('Current:       ', round(df2['Valor'].sum(),2))
print('%:             ', round(100*ret/port,2))
print('%, with div:   ', round(100*(ret + float(dividends.sum()))/port,2))

#Run Stats on History_paste:
df2.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Degiro/Output_csv/port_current.csv', index=False, header=True)

print('\nOver')