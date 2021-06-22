import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
pd.options.display.float_format = '{:,.5f}'.format


plot_ = 0
rolling_window = 70 
'''
ERROR!
CORRELATION IS FUCKED:


#Get Prices From a CSV FILE for a long time. 
---> NETFLIX & DISNEY



Why this ?
- When Covariances And overal Correlation ---> 1.0
---> LTCM Case. Respond to unstable market environments


'''

#Price Stock 1:
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Quant/Strat_Backtest/Pair_trading/Output_pair/NFLX_DIS.csv')
print(df)
price_1 = pd.DataFrame(df['NFLX'].values, columns = ['price_1'])
price_2 = pd.DataFrame(df['DIS'].values, columns = ['price_2'])




#MAKE IT returns:
price_1['returns'] = np.log(price_1['price_1']/price_1['price_1'].shift(1))
price_1.dropna(inplace=True)



#MAKE IT returns:
price_2['returns'] = np.log(price_2['price_2']/price_2['price_2'].shift(1))
price_2.dropna(inplace=True)


print('\n\nCOVARIANCE:\t')
print(price_1['returns'].iloc[:rolling_window].cov(other=price_2['price_2'].iloc[:rolling_window]))



#SAVE returnsURNS:
returns_1 = price_1['returns'].values.tolist()
returns_2 = price_2['returns'].values.tolist()


def square(list):
    return [i ** 2 for i in list]


ewma_1 = []
ewma_2 = []
cov_12 = []
def compute_ewma(list_returns_1,list_returns_2 ):
    returns_squared_1 = square(list_returns_1)
    returns_squared_2 = square(list_returns_2)

    covariance_numdays = np.cov(list_returns_1[:rolling_window], list_returns_2[:rolling_window])[0,1] #SOMETHING IS FISHY HERE ---
    covariance_numdays = covariance_numdays*(rolling_window/(rolling_window-1))

    print(covariance_numdays)
    print('\n')
    lambda_k = 0.94
    for row in range(len(list_returns_1)):
        #EWMA - STARTING AFTER 30 DAYS:
        if row == 0:
            print('1st row - Skipped') #WHY ?? - Only segund value gives an approximation to Variance

        if row < rolling_window : #DROP FIRST "X" Observations to compute Covariance
            ewma_1.append(returns_squared_1[row-1]) 
            ewma_2.append(returns_squared_2[row-1])

            cov_12.append(covariance_numdays)
        else:
            # EWMA 1
            decay = lambda_k * ewma_1[-1]
            added = (1-lambda_k) * (returns_squared_1[row-1])
            ewma_1.append(decay + added)

            # EWMA 2
            decay = lambda_k * ewma_2[-1]
            added = (1-lambda_k) * (returns_squared_2[row-1])
            ewma_2.append(decay + added)

            # Covariance
            decay = cov_12[-1] * lambda_k
            added = (1 - lambda_k) * list_returns_1[row-1] * list_returns_2[row-1] # CAREFUL WITH LAGS
            cov_12.append(decay+added)


    return ewma_1, ewma_2, cov_12




ewma_1, ewma_2, cov_12 = compute_ewma(returns_1, returns_2)

df_ewma = pd.DataFrame(ewma_1, columns = ['ewma_1'])
df_ewma['ewma_2'] = ewma_2
df_ewma['cov'] = cov_12

df_ewma['correlation'] = df_ewma['cov']/ ( (df_ewma['ewma_1']**.5) * (df_ewma['ewma_2']**.5) )

df_ewma = df_ewma[rolling_window:]
print(df_ewma.describe()) # FUCK!!! ERROR on CORRELATION:


print()
print(df_ewma)

df_ewma.plot()
plt.show()






'''
# COUNT - EWMA DATA:
print('\nEWMA_1 Counter:\t\t', len(ewma_1))
print('EWMA_2 Counter:\t\t', len(ewma_2))
print('COV_12 Counter:\t\t', len(cov_12))
'''





''' Rolling Volatility '''
# ROLLING VOLATILITY:
'''
price_1['vol'] = price_1['returns'].rolling(window=rolling_window).var()
price_1['vol'].dropna(inplace=True)

#COUNT - ROLLING Volatility:
number_vol = price_1['vol'].count()
print('Rolling Counter:\t',number_vol)
print('Total Returns:\t\t', price_1['returns'].count())
'''

'''Compare RESULTS '''
'''
df = pd.DataFrame(ewma_1[-number_vol:], columns=['ewma_1'])
df['rolling'] = price_1['vol'].iloc[-number_vol:].tolist()
#df['cumulative'] = returns[-number_vol:]
#df['cumulative'] = df['cumulative']/4

print('\n')
print(df.tail(3))


# PLotting GRAPH
if plot_ == 1:
    df.plot()
    plt.show()
'''