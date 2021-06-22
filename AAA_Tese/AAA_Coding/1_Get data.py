import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import numpy as np
import math

'''
def function(comments):
    List: 

    0:
    -Learn to do Risk Parity with all Data; (Done)
    -Get to know matrixes; (+-)

    1st:
    -Do VCV from past 2 Years and do a Risk-Parity Portfolio; (DONE)
    -Rearrange VCV Annually / Semiannually; (VERY IMPORTANT) *************


    1.5:
    -Do this with more ASSETS in Portfolio
    -PLOT CORRELATIONS across time
    -Plot Variances

    2nd:
    -Maximum Drawdown, biggest asset Changes? 
    -When return passes a certain Z value??

    3nd:
    -After getting the Switch button;
    -Change VCV with Forecasted VCV - CVCV
        * Model Variances - EWMA
        * Model Correlation

    4th:
    When to switch back the portfolio;
    There has to be a treshold.



    TICKERS:
    URTH -> iShares MSCI World ETF
    GOVT -> iShares U.S. Treasury Bond ETF
    ^GSPC --> S&P500

'''

#INPUTS
get_data = 0 #Download data Once
number_days = 756 #To compute first VCV
k = 252 #Pass values to annual for VCV - easier 

#DATES
start_date = '2012-12-31'
end_date = '2021-01-01'

#Tickers
list_tickers = ['^GSPC','GOVT', 'GLD'] #Added GOLD
name_columns = ['Stocks', 'Bond', 'Gold']


if get_data==1:
    #Table with Prices:
    df = pd.DataFrame(columns=list_tickers)

    #Fetch Data
    for ticker in list_tickers:
        df[ticker] = web.DataReader(ticker , 'yahoo', start=start_date, end=end_date)['Adj Close']
    df.columns = name_columns

    df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
else:
    df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
    df = df.set_index('Date')

df_returns = df.pct_change().dropna() #CHANGE TO df_ret
df_returns.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_returns.csv')


print(df.head(3))
print('\n')
print(df_returns.head(3))


#PLOT Cumulative returns
df=df.tail(252*3)
df = df/df.iloc[0]
df.plot()
plt.show()

'''
#Compute VCV from first 3 years: 2013-2016:
VCV = df_returns.head(number_days).cov() * k
print('VCV:\n',VCV)
VCV = VCV.values # Transform it to Matrix
'''
##############################################################################################################################
##############################################################################################################################


#w = ([0. , 1.]) # TESTING VALUES: FOR MCRi and portfolio Volatility

''' INPUT '''
'''
x= 21.556       #in Percentage
x =round(x/100,2) #Tranform
w = [ x , 1-x ] #Get Portfolio


std_p = math.sqrt(np.matrix(w) * VCV * np.matrix(w).T)

print('\n')
print('std_prt:\t', round(std_p*100,2), '%')

print('\n')
print('VCV Original\n', VCV)

number_rows = VCV.shape[0] 

MCR = [] 
for i in range(number_rows):
    MCR.append( (([row[i] for row in VCV] * np.matrix(w).T) / std_p ) * w[i]) # Missing Multiply by W_i
MCR = np.concatenate((MCR[0] , MCR[1]))




print('\nMCR FIRST:\n')
print(MCR)
'''


'''Check taht the MAth is Fine'''
'''
print('\n')
print('MCR_sum:\t', MCR.sum())
print('STD_prt:\t', std_p)

print('Ratio of MCR stocks-to-Bonds', MCR[0]/MCR[1]  )

print('\nDiff:\t', MCR[0]- MCR[1])
'''









'''
Now is the time to find the optimal Weights
Compute MCRi by changing Weights:

----> Do it by loop and increments:
Optimize instad of Manually:
A Minimizing Function.




'''

##############################################################################################################################
##############################################################################################################################


'''Return of Risk-Parity Portfolio '''
'''
rp_ret = df_returns
rp_ret['Stocks'] = rp_ret['Stocks']*w[0]
rp_ret['Bond'] = rp_ret['Bond']*w[1]

rp_ret['RP'] = rp_ret['Stocks'] + rp_ret['Bond'] 
#print(rp_ret)

rp_ret.tail(252*5).cumsum().plot() #For Last 3 Years
#rp_ret.tail((rp_ret.shape[0] - number_days)).cumsum().plot() #Since implementation
#plt.show()
'''

'''Plot Volatilities'''
'''
vol = pd.DataFrame()
vol['Stocks'] = df_returns['Stocks'].rolling(window=50).std() * 100
vol['Bond'] = df_returns['Bond'].rolling(window=50).std() * 100

vol['St/Bnd'] = vol['Stocks']/vol['Bond']
vol.dropna(inplace=True)

#print(vol)

vol.tail(252*5).plot()
#plt.show()
'''
print('\n')