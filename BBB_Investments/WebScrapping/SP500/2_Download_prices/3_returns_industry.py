import pandas as pd 

#import CSv
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv')
df2 = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/Prices_SP500_2010/df2_returns.csv')

print(df2.head())

#MAX = 119
biggest = 5

df.drop(inplace=True, columns=['sector'])

for i in range(biggest):
    print('Rank: ',i+1)
    print(df[df['industry']==df2['industry'][i]])
    print('\n')

#print(df2)
