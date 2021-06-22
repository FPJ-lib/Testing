import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt


print('\n\nStart\n')


start_date = '2021-02-26'
ratio_eurusd=1.2122


'''
Values from 7-May: Sunday
'''


#Ticker From Yahoo.Finance
tickers = ['DAC','EL.PA','GSL','HEIA.AS','ITX.MC', 'JMT.LS' ,'NVJP.DE' ,'VID.MC']
company = ['Danaos','essilor','Global Ship Lease','heineken','inditex','jeronimo','umicore','vidrala']
number_stocks = [8,4,12,7,8,50,10,3]
entry_price = [ round(39.43/ratio_eurusd,2) , 130, round(14.93/ratio_eurusd,2), 89.74, 25.7, 14.8194, 39.46, 76.2 ]
realized = [-0.53,-2.5,-0.53, -4.31 +(4.9-0.74), 8.82 + (2.8-0.53), 9.33+(25.63-8.97) , -4.2 + (5-1.5) , 3.33+22.19]

targets = [ round(80/ratio_eurusd,2) , 170,round(35/ratio_eurusd,2), 106, 34, 18, 70, 130]


#Create Arrays
price = pd.DataFrame(columns=tickers)
last_price = []


#Fetch Data

for ticker in tickers:
    #print(ticker)
    price[ticker] = web.DataReader(ticker , 'yahoo', start=start_date)['Adj Close']
    #print(price)
    last_price.append(round(price[ticker].iloc[-1],3))

#get UMICORE:
last_price[6] = 50.1

#Keep $ Values
danaos_price_usd = round(last_price[0],2)
gsl_price_usd = round(last_price[2],2)

last_price[0] = round(last_price[0]/ratio_eurusd,2)
last_price[2] = round(last_price[2]/ratio_eurusd,2)


#COMPILE:
data = {'company':  company,
        'ticker': tickers,
        'entry': entry_price,
        'price': last_price,
        'shares': number_stocks,
        'realized':realized
        }

df = pd.DataFrame (data, columns = ['company','ticker','entry','price','shares','realized'])

#Build Table
df['value'] = df['price'] * df['shares']
df['PnL'] = (df['price'] - df['entry']) * df['shares'] + df['realized']
df['pct, %'] = round( ( df['PnL']/df['value'] ) * 100,2)

#TARGETS: EXTRA
df['target'] = targets
df['tgt_pnl'] = (df['target']-df['entry'])*df['shares']


#Some stats:
profit = df['PnL'].sum()
profit = profit + 41.3 #Sell JMT
profit = round(profit, 2)

invested = (df['entry']*df['shares']).sum()
invested = round(invested, 2)

#WEIGHTS PORTFOLIO:
df['% portfolio'] = round(100 * df['value']/df['value'].sum(),2)

target = round(df['tgt_pnl'].sum(),2)
target_ret = round((target/invested)*100, 2)

#PRINT STATS:
print('##########'*8+ '##')
print (df[['company','ticker', 'entry', 'price','shares','value','PnL','pct, %']])

print('##########'*8+ '##')
print('Danaos USD price:\t$ %.2f' % danaos_price_usd, '|  $39.43 | ', round(100*(danaos_price_usd/39.24) - 100,2), '%' )
print('GSL USD price:\t\t$ %.2f' % gsl_price_usd, '|  $14.93 | ', round(100*(gsl_price_usd/14.93) - 100,2), '%' )

print('##########'*8 + '##')

print('PnL:\t\t', profit )
print('in %:\t\t', round( 100 * profit/invested, 2))
print('\nInvested:\t', invested)

'''
print('\nTarget:\t\t', target)
print('return:\t\t', target_ret,'%')
'''
print('##########'*8+ '##')
'''
__________________________________________________________________________
'''

'''
print('if equally weighted: \nreturn = ', round(df['pct, %'].sum()/8,2) ,'%')
print('profit = ', round((df['pct, %'].sum()/(8*100)) *invested,2) )
'''


print('\nOver')
