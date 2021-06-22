from sys import path
import pandas as pd 
import matplotlib.pyplot as plt

ticker ='JMT.LS'
statement = ['income-statement-', 'balance-sheet-', 'cash-flow-']
freq = ['annual', 'quarterly']

#import CSV:
path_csv ='/Users/filipepessoajorge/OneDrive/X02 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/WebScrapping/Financials_Statements/Firms_df/%s.csv' % ticker
df = pd.read_csv(path_csv)

df.index = df['Account']
df.drop(inplace=True, columns=['Account'])
print('\nDF_1st: \n', df)

#----------------------------------------------------REVIEW:
#Clean Data - Negatives & Float:
revenue = []
rev_growth = []
for i in range(5):
    name = 'Date -'+str(i)
    df[name] = df[name].str.replace(')','', regex=True)
    df[name] = df[name].str.replace('(','-', regex=True)
    df[name] = df[name].str.replace(',','', regex=True)
    df[name] = df[name].str.replace('--','0.', regex=True)
    df[name] = df[name].astype(float)
    
    revenue.append(df[name][1])

    df[name]= round(100 * df[name]/df[name].iloc[0], 2) #BETTER THIS ? 


print('\n\n\nSTART OF ALL:')
#print('\nRev: \n',revenue, '\n')

df.T['Revenue'] = revenue
print(df)

#REVENUES GROWTH
df = df.T
df['Revenue'] = round(100 * (df['Revenue']/df['Revenue'].shift(-1) - 1 ) ,2)
df = df.T

print('\n\nGROWTH-DONE\n')
print(df)
print('\n')
print('Company: ', ticker)






print('\n\n')