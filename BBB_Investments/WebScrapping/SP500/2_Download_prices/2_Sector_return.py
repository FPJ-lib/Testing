import pandas as pd
import math

'''
Another Way:
Go Through The tickers;
And calculate prices[ticker].mean()

Add directly to the DataFrame... Possible to add row by row??

'''

#import CSv
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv')
sector_df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/sector_industry.csv')
prices = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/Prices_SP500_2010/df.csv')

#Reduce Computing Power
print(prices.size)
prices = prices[-720:]
prices.dropna(inplace=True, axis = 1) #Drop Column of #NA
prices = prices.pct_change().dropna() 

stats = pd.DataFrame(columns=prices.columns)

for ticker in prices.columns:
    ret = prices[ticker].mean()
    ret=round(ret*100*360,2)

    std = prices[ticker].std()
    std = round(100 * math.sqrt(360) * std, 2)
    
    stats[ticker] = [ret, std, round(ret/std, 2) ]

#STATS for Pandas
stats = stats.T
stats.columns = ['Ret', 'Std', 'IS']
stats['ticker'] = stats.index

#Mergers 
df2 = stats.merge(df , how='left', on='ticker')

# CHANGE SHIT
df2 = df2.groupby(['industry']).mean()

df2 = df2.sort_values( by=['Ret'], ascending=False)
print (df2)

'''
EXPORT VALUES WITH COMPANY NAMES & RETURNS:


'''
df2.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/Prices_SP500_2010/df2_returns.csv')
print('\n\n')