import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 


''' INPUTS '''
get_data = 1

tickers_list = [
                
                ['GALP.LS', 'REP.MC' ], #0
                ['PEP', 'KO' ] , #1
                ['NFLX', 'DIS' ] , #2
                ['HEIA.AS', 'ABI.BR' ] , #3
                ['VZ', 'T' ], #4
                ['EDPR.LS', 'EDP.LS'], #5
                ['ALTR.LS', 'SEM.LS'], #Navigator
                [ 'SEM.LS', 'NVG.LS']

            ]   


start_date = '2014-12-31'
tickers = tickers_list[5]




''' FUNCTIONS '''
#2 tickers in List Format:
def get_prices(start_date, tickers_list):
    df = pd.DataFrame(columns=tickers_list)
    #Fetch Data
    for ticker in df.columns.to_list():
        print(ticker)
        df[ticker] = web.DataReader(ticker , 'yahoo', start=start_date)['Adj Close']

    return df

def get_comission(investment, variable_fee_percentage, fixed_fee):
    return abs(round(investment*(variable_fee_percentage/100) + fixed_fee, 3))



''' Code '''

print(tickers)
path = '/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Quant/Strat_Backtest/Pair_trading/Output_pair/%s.csv' % (tickers[0]+'_'+tickers[1])
if get_data == 1 :
    df = get_prices(start_date, tickers)
    df.to_csv(path)
else:
    df = pd.read_csv(path)

print('\ndf1: \n',df.tail(3))

#Reorganize Prices
#Make Higher Price on Numerator


df['ratio'] = df[tickers[0]]/df[tickers[1]]
print(df.tail(3))

# PLT RATIO
#df['ratio'].plot(title = tickers[0]+'/'+tickers[1])
#plt.show()




''' POSITIONS '''
long_st = 0

last_ratio = df['ratio'].iloc[-1]
print('\nLast Ratio: \t', last_ratio)


#Entry:
#   # Stocks
multiply = 1
st1 = 15.0 * multiply
#st2 = round((round(last_ratio, 4) * st1),0)
st2 = 59.0 * multiply




#Prices:
p1 = df[tickers[0]].iloc[-1]
p2 = df[tickers[1]].iloc[-1]
p1 = 17.58
p2 = 4.455

print('\n#1:', st1, '\n#2:',st2)

st1_cost = round(st1 * p1,3)
st2_cost = round(st2 * p2,3)
net = round(-st1_cost + st2_cost,3) if long_st==1 else round(st1_cost - st2_cost,3)



#Comissions:
''' Review COMISSION RATE '''

comission1 = get_comission(st1_cost, 0.06,0.5)
comission2 = get_comission(st2_cost, 0.06,0.5)
comissionT = round(comission1 + comission2,3)

print('\nTotal Comission:\t', comissionT)
print('Stock 1 - ',tickers[0],':\t', -st1_cost if long_st==1 else st1_cost )
print('Stock 2 - ',tickers[1],':\t', st2_cost  if long_st==1 else -st2_cost  )
print('Net: \t\t\t' , round(net - comissionT,3))
print('\nRatio Entry:\t\t\t', round(p1/p2,2))


scenarios = [
    [16.5, 4.7], #Best
    [18.1, 4.35], #Worst
    [ round(df[tickers[0]].iloc[-1],3), round(df[tickers[1]].iloc[-1],3)] #Current
]

print('_-'*20)
for scenario in scenarios:

    print('Scenario: \t',scenario)

    p1_out = scenario[0]
    p2_out = scenario[1]

    comission1_out = get_comission(st1 * p1_out,0.06, 0.5)
    comission2_out = get_comission(st2 * p2_out, 0.0006, 0.5)
    comissionT_out = round(comission1_out + comission2_out,3)

    net1 = (p1_out-p1)*st1  if long_st else  (p1-p1_out)*st1 
    net1 = round(net1,3)
    net2 = (p2-p2_out)*st2  if long_st else  (p2_out-p2)*st2 
    net2 = round(net2,3)

    ret = round(net1+net2-comissionT-comissionT_out,3)
    ret_p = round( 100 * ret / max(st1_cost, st2_cost),3)

    print('Ratio: \t\t\t\t', round(p1_out/p2_out,2))
    print('Gain - St1 - ', tickers[0],': \t', net1 )
    print('Gain - St2 - ', tickers[1],': \t\t', net2 )
    print('\nNet: \t\t\t\t', round(net1+net2,2) )
    print('Total Comission:\t\t', -round(comissionT+comissionT_out,2) )
    print('Net of comission: \t\t', ret)
    print('Return:\t\t\t\t', ret_p, '%')
    print('_-'*20)




#df[tickers[0]].plot(legend = tickers[0])
#df[tickers[1]].plot(legend = tickers[1])
#plt.show()

#df[tickers[0]].rolling(window=50).corr(other=df[tickers[1]]).plot(legend = 'Correlation')
#plt.show()

df['ratio'].iloc[-150*2:].plot(title = tickers[0]+'/'+tickers[1])
#plt.show()


print('Last prices: ', scenarios[-1])
print('\nThe End\n')