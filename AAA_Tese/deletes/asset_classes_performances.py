import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt

'''
Missing: 
Do Portfolios. Equal weight. Minimum variance. 


Objective:
-Market Correlations in times of uncertainty.
-The addition of a new market player --- Central Banks. 

-# Cases of COVID and Market Conditions.
-Unemployment

'''

# 2008 Crisis:
'''
start_date = '2006-09-30'
end_date ='2011-01-01'
'''

#2016 to 2018, Trump election:
'''
start_date = '2015-09-30'
end_date ='2018-01-01'
'''


#COVID

start_date = '2017-12-31'
end_date ='2021-01-01'


last_number_days = 400

'''
#complete
list_tickers= ['EEM','EWJ','EWY','IWM','TLT','IAU','FXI','XCH.TO','IGIB','ISTB']
name_columns = ['Emrg','JPN','SK','RSS2k','20Y TB','GLD','CHN LrgCap','CHN ETF','Corp Bonds','1-5Y USD Bond']
'''

list_tickers= ['EEM','IWM','TLT','IAU','IGIB','ISTB']
name_columns = ['Emrg','RSS2k','20Y TB','GLD','Corp Bonds','1-5Y USD Bond']



#Table with Prices:
df = pd.DataFrame(columns=list_tickers)

#Fetch Data
for ticker in list_tickers:
    df[ticker] = web.DataReader(ticker , 'yahoo', start=start_date, end=end_date)['Adj Close']

#Get Cumulative return
df = df/df.iloc[0]
print(df)

#Rename & Plot:
df.columns = name_columns
df.plot()


#Get Correlation in TIME:
#correlation_rolling = df.rolling(window=100).corr()
#print(correlation_rolling)


#correlation_rolling.plot()

#Plot last ??? days
#df[-last_number_days:].plot()
plt.show()