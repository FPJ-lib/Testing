import pandas as pd 
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

'''
Confirm Values of the Compute_ewma function. the row-1 should be row?
Covariance and Covariances all in the same rows. Include the Index.

'''

pd.options.display.float_format = '{:,.5f}'.format

#Switches:
get_data = 0
rolling_window = 50
lambda_k = 0.94


#DATES
start_date = '2012-12-31'
end_date = '2021-01-15'

#Tickers
list_tickers = ['^GSPC','GOVT', 'EEM','GLD'] #Added GOLD
name_columns = ['SP', 'Bond','EM', 'Gold']


if get_data==1:
    #Table with Prices:
    df = pd.DataFrame(columns=list_tickers)

    #Fetch Data
    for ticker in list_tickers:
        df[ticker] = web.DataReader(ticker , 'yahoo', start=start_date, end=end_date)['Adj Close']
    df.columns = name_columns

    df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_001.csv')
else:
    df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_001.csv')
    df = df.set_index('Date')


df_returns = df.pct_change().dropna() #CHANGE TO df_ret
df_returns.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_returns_001.csv')


#Check Data
print('Data:\n', df)
print('\nReturns:\n', df_returns)




''' Function to get EWMA between 2 Securities '''

ewma_1 = []
ewma_2 = []
cov_12 = []

def square(list):
    return [i ** 2 for i in list]

ewma = []
def compute_ewma(list_returns):
    ewma = []
    returns_squared = square(list_returns)

    print('\n')
    
    for row in range(len(list_returns)):
        #print(list_returns[row], '\t\t', returns_squared[row])

        if row == 0:
            print('1st row - Skipped')
        elif row < rolling_window :
            value_append = returns_squared[row-1] #Drop X Variables - "returns squared for the last"
            ewma.append(value_append)
        else:
            decay = lambda_k * ewma[-1] #With 1st significant Value for the returns^2
            added = (1-lambda_k) * (returns_squared[row-1])
            ewma.append(decay + added)
    return ewma #Should drop ROLLINGWINDOW Observations? Probabily



df_ewma = pd.DataFrame()

i=1
for column in name_columns:
    df_ewma[column] = compute_ewma(df_returns[column].values) #compute each individually

print('\nEWMA Volatilities:\n', df_ewma)
print('Size_EWMA:\t', df_ewma.shape)
print('Size_Returns:\t', df_returns.shape)


''' So Far So Good '''



df_covariances = pd.DataFrame()
#Compute all the covariances in the matrix
for num_row in range(1,len(name_columns)):
    for num_col in range(num_row+1,len(name_columns)):
        print('#row:\t', num_row)
        print('#col:\t', num_col)
        print('\n')

        





