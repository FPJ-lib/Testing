import pandas as pd


#import CSV
df= pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Degiro/Account/Account.csv')

'''
Current Output:
--Dividends & Tax on Dividends:

Next:
--Costs of Stock Exchange:
(New file Maybe)


'''

df.drop(inplace = True, columns=['Hora','Data Valor','ISIN','T.','Mudança','Saldo','ID da Ordem'])
df.rename(columns={'Unnamed: 8': 'Amount' }, inplace = True )

#Sum AMOUNTS:: 
df.drop(inplace = True, columns = ['Data', 'Unnamed: 10']) # Descrição
#print(df)

#Get Amount to Number
df['Amount']=df['Amount'].str.replace(",",".")
df['Amount'] = pd.to_numeric(df['Amount'], downcast='float')
#print(df.dtypes)

#df=df.groupby(['Descrição', 'Produto']).sum()
df['Amount']=round(df['Amount'],2)
#print(df.sort_values(by=['Descrição']))

df = df[ ( df['Descrição']=='Imposto sobre dividendo') | (df['Descrição']=='Dividendo') ]
df=df.groupby(['Produto','Descrição']).sum()

print(df)
print('\nTotal Dividends: \n', df['Amount'].sum())

df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Degiro/Output_csv/Dividends_and_Tax.csv')

#print(df)
print('\nOver\n')