import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

'''
Do Correlations Correctly!

WTF! Why is it wrong??


'''


df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
df = df.set_index('Date')
print(df)

df.drop('Gold', axis =1 , inplace=True)

print(df)

df = np.log(df/df.shift(1))

print(df)

print('\n\n')

filter_index = df[df['Stocks'].isna()].index.values
print(filter_index)

konstant = 0.94

#Restrict Data
#df= df.tail(-252*2)

def get_EWMA(df, columns_name):
    volatility = []
    for row in range(len(df)):

        if row==0:
            volatility.append(0)
        elif row ==1:
            vol = (df[columns_name].iloc[row] )**2
            volatility.append( vol )
        else:
            vol = (volatility[-1]**2)*konstant  + (1-konstant)* ((df[columns_name].iloc[row-1])**2)
            volatility.append(  vol )
    return volatility
    #print(volatility)

def get_EWMA_Covariance(df, columns_name = ['Stocks','Bond']):
    covar = []
    for row in range(len(df)):
        if row < 21 :
            covar.append(0)
        elif row == 21 :
            cov = df[['Stocks','Bond']].iloc[1:21].cov().values
            print(cov)
            covar.append(cov[0][1])
        else:
            cov = (covar[-1])*konstant  + (1-konstant)* ( (df[columns_name[0]].iloc[row-1]) * (df[columns_name[1]].iloc[row-1]) )
            covar.append(  cov )
            #print(cov)
    #print(covar)
    return covar

def get_EWMA_Correlation(df):
    corr = []
    for row in range(len(df)):
        if row < 21 :
            corr.append(0)
        else :
            corr = df['Cov'].iloc[row] / ( (df['St_EWMA'].iloc[row]**0.5) * (df['Bd_EWMA'].iloc[row]**0.5)  )
            print(corr)
            #corr.append(corr)
    #print(covar)
    return corr



df['St_EWMA'] = get_EWMA(df, 'Stocks')
df['St_EWMA'] = (df['St_EWMA']**0.5) 

df['Bd_EWMA'] = get_EWMA(df, 'Bond')
df['Bd_EWMA'] = (df['Bd_EWMA']**0.5) 

df['Cov'] = get_EWMA_Covariance(df)
df['St*st'] = df['Bd_EWMA'] * df['St_EWMA'] 


#df['Correlation'] = get_EWMA_Correlation(df)
df['Correlation'] = df['Cov'] / df['St*st']
#print('iLOC[10\n\n', df.iloc[10])


#Last months
#df = df.tail(300)


df['Cumulative_St'] = df['Stocks'].cumsum()
df['Cumulative_Bd'] = df['Bond'].cumsum()


pd.options.display.float_format = '{:.5f}'.format #This worked last time
print(df)

print(df['St_EWMA'][-1] * (252**0.5))



'''
                            PLOTTING
'''




'''
df['St_EWMA'].plot()
df['Cumulative_St'].plot()
#plt.show()


df['Bd_EWMA'].plot()
df['Cumulative_Bd'].plot()
#plt.show()
'''

#df['Correlation'].plot()
#plt.show()





print(df)
print('\n\n')