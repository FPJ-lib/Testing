'''
SHITTY

'''


#https://www.pythonforfinance.net/2016/09/01/moving-average-crossover-trading-strategy-backtest-in-python/
import pandas as pd
import numpy as np
from pandas_datareader import data
import matplotlib 
from matplotlib  import pyplot as plt

sp500 = data.DataReader('^GSPC', 'yahoo',start='1/1/2000')

print(sp500.head())

#Check Graph
#sp500['Close'].plot(grid=True,figsize=(8,5))
#plt.show()

'''
Cross over of 2 MA's
2M --> 42  days
1Y --> 252 days
'''

sp500['42d'] = np.round(sp500['Close'].rolling(window=42).mean(),2)
sp500['252d'] = np.round(sp500['Close'].rolling(window=252).mean(),2)

#sp500[['Close','42d','252d']].plot(grid=True,figsize=(8,5))

'''
We will have 3 basic states/rules:

1) Buy Signal (go long) – the 42d moving average is for the first time X points above the 252d tend.

2) Park in Cash – no position.

3) Sell Signal (go short) – the 42d moving average is for the first time X points below the 252d trend.

'''

sp500['42-252'] = sp500['42d'] - sp500['252d']

#X was arbitrary
X = 50
sp500['Stance'] = np.where(sp500['42-252'] > X, 1, 0)
sp500['Stance'] = np.where(sp500['42-252'] < -X, -1, sp500['Stance'])
#print(sp500['Stance'].value_counts())

#Graph
#sp500['Stance'].plot(lw=1.5,ylim=[-1.1,1.1])
#plt.show()

sp500['Market Returns'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Market Returns'] * sp500['Stance'].shift(1)


#Strategy Output
#sp500[['Market Returns','Strategy']].cumsum().plot(grid=True,figsize=(8,5))
#plt.show()





'''


Link to more complete Strategy Check

https://www.pythonforfinance.net/2016/09/02/analysis-of-moving-average-crossover-strategy-backtest-returns-using-pandas/

'''



#STRATEGY BACKTEST

#https://www.pythonforfinance.net/2016/09/02/analysis-of-moving-average-crossover-strategy-backtest-returns-using-pandas/
#import relevant modules
import pandas as pd
import numpy as np
from pandas_datareader import data
from math import sqrt
import matplotlib.pyplot as plt


#download data into DataFrame and create moving averages columns
sp500 = data.DataReader('^GSPC', 'yahoo',start='1/1/2000')
sp500['42d'] = np.round(sp500['Close'].rolling(window=42).mean(),2)
sp500['252d'] = np.round(sp500['Close'].rolling(window=252).mean(),2)

#create column with moving average spread differential
sp500['42-252'] = sp500['42d'] - sp500['252d']

#set desired number of points as threshold for spread difference and create column containing strategy 'Stance'
X = 50
sp500['Stance'] = np.where(sp500['42-252'] > X, 1, 0)
sp500['Stance'] = np.where(sp500['42-252'] < X, -1, sp500['Stance'])
sp500['Stance'].value_counts()

#create columns containing daily market log returns and strategy daily log returns
sp500['Market Returns'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Market Returns'] * sp500['Stance'].shift(1)

#set strategy starting equity to 1 (i.e. 100%) and generate equity curve
sp500['Strategy Equity'] = sp500['Strategy'].cumsum() + 1

#show chart of equity curve
#sp500['Strategy Equity'].plot()

'''
1) Charting section – we will create charts for the following series:
a) Rolling 1 year annualised volatility
b) Rolling 1 year hit ratio
c) Rolling 1 year returns
d) Daily return chart
e) Daily return distribution histogram
'''

strat = pd.DataFrame([sp500['Strategy Equity'], sp500['Strategy']]).transpose()

#create columns that signifies whether each days return was positive, negative or flat.
strat['win'] = (np.where(strat['Strategy'] > 0, 1,0)) 
strat['loss'] = (np.where(strat['Strategy'] < 0, 1,0)) 
strat['scratch'] = (np.where(strat['Strategy'] == 0, 1,0)) 

#create columns with a cumulative sum of each of the columns created above 
strat['wincum'] = (np.where(strat['Strategy'] > 0, 1,0)).cumsum() 
strat['losscum'] = (np.where(strat['Strategy'] < 0, 1,0)).cumsum() 
strat['scratchcum'] = (np.where(strat['Strategy'] == 0, 1,0)).cumsum() 

#create a columns that holds a running sum of trading days - we will use this to create our percentages later 
strat['days'] = (strat['wincum'] + strat['losscum'] + strat['scratchcum']) 

#create columns that shows the 252 day rolling sum of the winning/losing/flat days 
strat['rollwin'] = strat['win'].rolling(window=252).sum() 
strat['rollloss'] = strat['loss'].rolling(window=252).sum() 
strat['rollscratch'] = strat['scratch'].rolling(window=252).sum() 

#create columns with hit ratio and loss ratio data 
strat['hitratio'] = strat['wincum'] / (strat['wincum']+strat['losscum']) 
strat['lossratio'] = 1 - strat['hitratio'] 

#create columns with rolling 252 day hit ratio and loss ratio data 
strat['rollhitratio'] = strat['hitratio'].rolling(window=252).mean() 
strat['rolllossratio'] =1 - strat['rollhitratio'] 

#create column with rolling 12 month return 
strat['roll12mret'] = strat['Strategy'].rolling(window=252).sum() 

#create column with average win, average loss and average daily return data 
strat['averagewin'] = strat['Strategy'][(strat['Strategy'] > 0)].mean() 
strat['averageloss'] = strat['Strategy'][(strat['Strategy'] < 0)].mean() 
strat['averagedailyret'] = strat['Strategy'].mean() 

#create column with rolling 1 year daily standard deviation and rolling 1 year annualised standard deviation
strat['roll12mstdev'] = strat['Strategy'].rolling(window=252).std() 
strat['roll12mannualisedvol'] = strat['roll12mstdev'] * sqrt(252)



#All graphs

#strat['roll12mannualisedvol'].plot(grid=True, figsize=(8,5),title='Rolling 1 Year Annualised Volatility')
#strat['rollhitratio'].plot(grid=True, figsize=(8,5),title='Rolling 1 Year Hit Ratio')
#strat['roll12mret'].plot(grid=True, figsize=(8,5),title='Rolling 1 Year Returns')
#strat['Strategy'].plot(grid=True, figsize=(8,5),title='Daily Returns')
#strat['Strategy'].plot(kind='hist',figsize=(8,5),title='Daily Return Distribution',bins=100)


#plt.show()
print("Skew:",round(strat['Strategy'].skew(),4))
print("Kurtosis:",round(strat['Strategy'].kurt(),4))
print("\n")



#############   KPI's   #############

'''
1) Annualized Return
2) Last 12 months Return
3) Volatility
4) Sharpe Ratio
5) Maximum Drawdown
6) Calmar Ratio (Annualized Return / Maximum Drawdown)
7) Volatility / Maximum Drawdown
8) Best Month Performance
9) Worst Month Performance
10) % of Profitable Months & % Non-Profitable Months
11) Number of Profitable Months/Number of Non Profitable Months
12) Average Monthly Profit
13) Average Monthly Loss
14) Average Monthly Profit/Average Monthly Loss
'''

#Create a new DataFrame to hold our monthly data and populate it with the data from the daily returns column of our 
#original DataFrame and sum it by month
stratm = pd.DataFrame(strat['Strategy'].resample('M').sum())

#Build the monthly data equity curve
stratm['Strategy Equity'] = stratm['Strategy'].cumsum()+1

#Add a column that holds the numerical monthly index (i.e. Jan = 1, Feb = 2 etc)
stratm['month'] = stratm.index.month




#1) Annualised Return
    
days = (strat.index[-1] - strat.index[0]).days
cagr = ((((strat['Strategy Equity'][-1]) / strat['Strategy Equity'][1])) ** (365.0/days)) - 1
print ('CAGR =',str(round(cagr,4)*100)+"%")
print("\n")


#2) Last 12 months Return

stratm['last12mret'] = stratm['Strategy'].rolling(window=12,center=False).sum()
last12mret = stratm['last12mret'][-1]
print('last 12 month return =',str(round(last12mret*100,2))+"%")
print("\n")


#3) Volatility
voldaily = (strat['Strategy'].std()) * sqrt(252)
volmonthly = (stratm['Strategy'].std()) * sqrt(12)
print ('Annualised volatility using daily data =',str(round(voldaily,4)*100)+"%")
print ('Annualised volatility using monthly data =',str(round(volmonthly,4)*100)+"%")
print("\n")


#4) Sharpe Ratio
dailysharpe = cagr/voldaily
monthlysharpe = cagr/volmonthly
print ('daily Sharpe =',round(dailysharpe,2))
print ('monthly Sharpe =',round(monthlysharpe,2))
print("\n")

'''
#5) Maxdrawdown

#Create max drawdown function
def max_drawdown(X):
    mdd = 0
    peak = X[0]
    for x in X:
        if x > peak: 
            peak = x
        dd = (peak - x) / peak
        if dd > mdd:
            mdd = dd
    return mdd  


mdd_daily = max_drawdown(strat['Strategy Equity'])
mdd_monthly = max_drawdown(stratm['Strategy Equity'])
print ('max drawdown daily data =',str(round(mdd_daily,4)*100)+"%")
print ('max drawdown monthly data =',str(round(mdd_monthly,4)*100)+"%")
print("\n")



#6) Calmar Ratio
calmar = cagr/mdd_daily
print ('Calmar ratio =',round(calmar,2))
print("\n")


#7 Volatility / Max Drawdown
vol_dd = volmonthly / mdd_daily
print ('Volatility / Max Drawdown =',round(vol_dd,2))
print("\n")

'''
#8) Best Month Performance
bestmonth = max(stratm['Strategy'])
print ('Best month =',str(round(bestmonth,2))+"%")


#9) Worst Month Performance
worstmonth = min(stratm['Strategy'])
print ('Worst month =',str(round(worstmonth,2)*100)+"%")
print("\n")

#10) % of Profitable Months & % Non-Profitable Months
positive_months = len(stratm['Strategy'][stratm['Strategy'] > 0])
negative_months = len(stratm['Strategy'][stratm['Strategy'] < 0])
flatmonths = len(stratm['Strategy'][stratm['Strategy'] == 0])
perc_positive_months = positive_months / (positive_months + negative_months + flatmonths)
perc_negative_months = negative_months / (positive_months + negative_months + flatmonths)
print ('% of Profitable Months =',str(round(perc_positive_months,2)*100)+"%")
print ('% of Non-profitable Months =',str(round(perc_negative_months,2)*100)+"%")
print("\n")

#11) Number of Profitable Months/Number of Non Profitable Months
prof_unprof_months = positive_months / negative_months
print ('Number of Profitable Months/Number of Non Profitable Months',round(prof_unprof_months,2))
print("\n")

#12) Average Monthly Profit
av_monthly_pos = (stratm['Strategy'][stratm['Strategy'] > 0]).mean()
print ('Average Monthly Profit =',str(round(av_monthly_pos,4)*100)+"%")


#13) Average Monthly Loss
av_monthly_neg = (stratm['Strategy'][stratm['Strategy'] < 0]).mean()
print ('Average Monthly Loss =',str(round(av_monthly_neg*100,2))+"%")
print("\n")

#14) Average Monthly Profit/Average Monthly Loss
pos_neg_month = abs(av_monthly_pos / av_monthly_neg)
print ('Average Monthly Profit/Average Monthly Loss',round(pos_neg_month,4))
print("\n")


monthly_table = stratm[['Strategy','month']].pivot_table(stratm[['Strategy','month']], index=stratm.index, columns='month', aggfunc=np.sum).resample('A')
monthly_table = monthly_table.aggregate('sum')

#Drop the top level column index which curently shows as "Strategy"
monthly_table.columns = monthly_table.columns.droplevel()


#replace full date in index column with just the correspnding year
monthly_table.index = monthly_table.index.year

#Replace integer column headings with MMM format
monthly_table.columns = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

print(monthly_table.head(17))

print("\n")
