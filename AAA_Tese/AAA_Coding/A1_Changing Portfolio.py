import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


#Data
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
df = df.set_index('Date')
print(df)

df = df.tail(252*5)

#Returns
df_returns = pd.DataFrame(np.log(df/df.shift(1)))
print(df_returns)

#Volatility
df_vol = df_returns.rolling(window=50).std()
print(df_vol)

#df_vol.plot()
#plt.show()

switch = df_vol
switch['Corr'] = df_returns['Stocks'].rolling(window=50).corr(other=df_returns['Bond'])
switch['Rat'] = switch['Stocks'] / switch['Bond']
switch['Corr * Rat'] = switch['Corr'] * switch['Rat']
print(switch)


''' PLOT SUBGRAPHS '''
# The GRAPH1 plot consisting of dailing closing prices
cumulative = plt.subplot2grid((7, 6), (0, 0), rowspan=3, colspan=6)
cumulative.plot(df_returns.cumsum(), label='Cumulative')
#cumulative.plot(portfolio_return, label='15-85' )
plt.title('Cumulative Returns')
plt.legend(loc=2)

# The GRAPH2 plot consisting of dailing closing prices
volatility = plt.subplot2grid((7, 6), (3, 0), rowspan=2, colspan=6)
volatility.plot(df_vol[['Stocks','Bond','Gold']], label='Last')
plt.title('Volatilities')
#plt.legend(loc=2)

# The GRAPH3 plot consisting of dailing closing prices

vol_ratio = plt.subplot2grid((7, 6), (5, 0), rowspan=2, colspan=6)
vol_ratio.plot(switch[['Corr','Rat','Corr * Rat']], label='Stock/ Bond')
plt.title('Stock/ Bond')


print(df_vol)


#plt.gcf().set_size_inches(8, 8)
#plt.subplots_adjust(hspace=0.75)
print('\nPRE-CHART\n')
plt.show()

print('The End')