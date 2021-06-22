import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt


print()


start_date = '2021-02-20'
ratio_eurusd=1.212252141


'''
Values from 21-February: Sunday
'''


#Ticker From Yahoo.Finance
tickers = ['DAC','EL.PA','GSL','HEIA.AS','ITX.MC', 'JMT.LS' ,'NVJP.DE' ,'VID.MC']

#Create Arrays
price = pd.DataFrame(columns=tickers)

price = web.DataReader(['JMT.LS'] , 'yahoo', start=start_date)['Adj Close']

print(price)