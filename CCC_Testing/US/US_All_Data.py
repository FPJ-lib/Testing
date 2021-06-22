import quandl
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

quandl.ApiConfig.api_key = 'QRisxrNExze-5RCysH3-'

plot = 1
linreg = 1

#GET DATA
df = quandl.get(['FRED/DEXUSEU','FRED/DTWEXBGS','FRED/CPIAUCSL','FRED/DFF','FRED/DTB3','FRED/DGS5','FRED/DGS10','FRED/DGS30','FRED/DPRIME'],\
    trim_start="2015-1-1", trim_end="2021-12-12", collapse = 'monthly')
df.columns = ['EUR/USD','USD','Infl','Eff Fed', '3m', '5Y', '10Y','30Y','Bank Prime Loan']
df['Infl']= round(df['Infl'].pct_change() *100,5)
df['USD']= round(df['USD'].pct_change() *100,5)
print(df)

#INTERESTING --- DATA:
plotter = df[['EUR/USD','USD','Infl','Eff Fed']]
plotter['EUR/USD']= round(plotter['EUR/USD'].pct_change() *100,5) #Change if EURUSD -->USD

plotter = plotter.dropna()
plotter['Real_rate'] = plotter['Eff Fed'] - plotter['Infl'] 
print(plotter)

#Plot:
if plot == 1:
    plotter[['EUR/USD','Real_rate']].plot()
    plt.show()

print(plotter.corr())

# Get in variables
x = plotter['EUR/USD']
y = plotter['Real_rate']

if plot==1:
    # PLOT Data
    plt.scatter(x,y, marker='1')
    plt.xlabel('€/$')
    plt.ylabel('Eff rate - Infl')

    #Plot Regression
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*x +b )

    plt.show()

#LIN-REGRESSION
#https://365datascience.com/linear-regression/

if linreg==1:
    beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)

    print('\n')
    print('Beta:    ', round(beta,4), \
        '\nAlpha:   ', round(alpha,4),\
        '\nR^2:     ', round(r_value**2,4), \
        '\nP-value: ', round(p_value,4), \
        '\nstd_err: ', round(std_err,4))
    print('\n')

print('Over')