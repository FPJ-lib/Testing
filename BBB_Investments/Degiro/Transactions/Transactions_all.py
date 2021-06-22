import pandas as pd
import numpy as np

'''
Cost of each Stock + Fees

Output:
-Current Portfolio Cost
-Profit & Loss of Closed Positions

Flaws:
* Products with many transactions (open and closing many times)

'''

df= pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Degiro/Transactions/Transactions.csv')
df.drop(inplace=True, columns=['ID da Ordem', "Taxa de Câmbio", 'Valor local', 'ISIN', 'Unnamed: 15','Unnamed: 10','Unnamed: 8','Unnamed: 6','Hora','Unnamed: 13' ])
df.drop( inplace=True, columns=['Data', 'Preços','Total'])
df = df.groupby(['Produto']).sum()
df['Total'] = df['Valor'] + df['Taxa']
df.sort_values(inplace=True, by=['Quantidade'], ascending=False)

#Delete Closed Positions:
df['Quantidade'] = df['Quantidade'].replace(0, np.nan)
portfolio_cost = df.dropna()

#PnL of Closed Positions:
pnl = df[df['Quantidade'] != 0].sum()  - portfolio_cost.sum()
pnl.drop(inplace=True, columns=['Quantidade'])

print(df, '\n')
print(portfolio_cost, '\n')

print('Profit_and_Loss: ')
print(pnl)


#Save it to OUTPUT_CSVS- To use For Portfolio::
portfolio_cost.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Degiro/Output_csv/portfolio_cost.csv', index=True)
pnl.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Degiro/Output_csv/pnl.csv', index=True, header=False)

print('Over')