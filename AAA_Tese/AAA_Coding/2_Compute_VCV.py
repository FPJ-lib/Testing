import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans



#Data
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
df = df.set_index('Date')
print(df)

#Returns
df_returns = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_returns.csv')
df_returns = df_returns.set_index('Date')
print(df_returns)

#Volatility
df_vol = df_returns.rolling(window=50).std()
print(df_vol)


#Test MACHINE LEARNING K- Cluster
print('\n\nStart\n\n')

df2 = df_vol.dropna()
model = KMeans(n_clusters=3)
model = model.fit(df2)

print('\nSTRT K Cluster\n')
print(model.cluster_centers_)
print(model.labels_)
print('\nEND K Cluster\n')

df2["Group"] = model.labels_
print(df2)
print(df2['Group'].sort_values())
print(df2['Group'].sum())
df2['Group'] = df2['Group']/50

df2.plot()
plt.show()

print('\n\nEND\n\n')
#Cumulative
df_cumulative = df
df_cumulative = df_cumulative / df_cumulative.iloc[0]
#print(df_cumulative)

#Correlation
df_correlation = df_returns['Stocks'].rolling(window=50).corr(df_returns['Bond'])
#print(df_correlation)


# Portfolio:
x = 0.17
w = [x, 1-x]

portfolio_return = df['Stocks'] * w[0] + df['Bond'] * w[1]
portfolio_return = portfolio_return / portfolio_return.iloc[0]
print(portfolio_return)


portfolio_return = portfolio_return/portfolio_return.shift(1) -1
print(portfolio_return)
print('\n\nStd:\n %f ' % (portfolio_return.std() * 252) ,'%' )
print('\nStd_securities:\n\n', df_returns.std()*252 )
print('\n')


print('\n\nReturn:\n %f ' % (portfolio_return.mean() *100* 252) ,'%' )
print('Return_securities:\n\n', df_returns.mean()*100*252 )
print('\n')




''' PLOT SUBGRAPHS '''
# The GRAPH1 plot consisting of dailing closing prices
cumulative = plt.subplot2grid((6, 6), (0, 0), rowspan=2, colspan=6)
cumulative.plot(df_cumulative, label='Cum')
cumulative.plot(portfolio_return, label='15-85' )
plt.title('Cumulative Returns')
plt.legend(loc=2)

# The GRAPH3 plot consisting of dailing closing prices
volatility = plt.subplot2grid((6, 6), (2, 0), rowspan=2, colspan=6)
volatility.plot(df_vol, label='Last')
plt.title('Volatilities')
#plt.legend(loc=2)

# The GRAPH4 plot consisting of dailing closing prices
correlation = plt.subplot2grid((6, 6), (4, 0), rowspan=2, colspan=6)
correlation.plot(df_correlation, label='Corr')
plt.title('Correlation')
#plt.legend(loc=2)


plt.gcf().set_size_inches(8, 8)
plt.subplots_adjust(hspace=0.75)
#plt.show()

