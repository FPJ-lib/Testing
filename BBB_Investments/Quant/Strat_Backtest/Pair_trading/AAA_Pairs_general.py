import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 


''' INPUTS '''
get_data = 1

# Long on the Ratio = 1; Short=0;
''' Make the Long_st automatic '''
long_st = 1
value = 500

init_fee_1 = 0.5
init_fee_2 = 0.5

target_ratio = 4.8


#Inputs: #PLOTS & MATH
plot_ratio = 1
plot_prices = 0
num_days = 22*5


tickers_list = [
                
                ['GALP.LS', 'REP.MC' ], #0
                ['PEP', 'KO' ] , #1
                ['NFLX', 'DIS' ] , #2
                ['HEIA.AS', 'ABI.BR' ] , #3
                ['VZ', 'T' ], #4
                ['EDPR.LS', 'EDP.LS'], #5
                ['SEM.LS','ALTR.LS' ], #SEMAPA , ALTRI (YES)           , #6
                [ 'SEM.LS', 'NVG.LS'], # SEMAPA OWNS 69.4% of NAVIGATOR , #7
                [ 'ALTR.LS','NVG.LS'], # COMPETITORS, NAVIGATOR HIGHER REV , #8
                ['VOW.DE','VOW3.DE'] # Ordinary VS Prefered Shares(most liquid)

            ]   

# 8 --> Too Look for: ALTRI VS NAVIGATOR --> Why their perspectives are so different
#-1 --> Ordinary over preference --> Preference has no voting rights


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
    return abs(round(abs(investment)*(variable_fee_percentage/100) + fixed_fee, 3))

def open_position(entry_data, long_st):
    #GET STOCKS NUMBERS:
    st1 = entry_data['num_stock'][0]
    st1 = st1 if long_st else -st1 
    
    #MAKE IT with SIGNALS:
    st2 = entry_data['num_stock'][1] 
    st2 = -st2 if long_st else st2

    #GET PRICES:
    p1 = entry_data['price'][0]
    p2 = entry_data['price'][1]

    #VALUES:
    value1 = round(st1*p1,3)
    value2 = round(st2*p2,3)
    
    #GET COMISSIONS:
    comission1 = get_comission(value1, 0.05, entry_data['fixed_fee'][0])
    comission2 = get_comission(value2, 0.05, entry_data['fixed_fee'][1])    
    comissionT = round(comission1 + comission2, 2)

    #PRINT:
    print('\n#1:', st1, '\n#2:', st2)
    print('\nStock 1 - ',tickers[0],':\t', round(value1,2) )
    print('Stock 2 - ',tickers[1],':\t', round(value2,2) )
    print('Total Comission:\t', comissionT)
    print('Net: \t\t\t' , round(value1 + value2 - comissionT, 2) )
    print('\nRatio:\t\t\t\t', round(p1/p2,3))

    #FOR FURTHER USE:
    entry_data['num_stock'] = [st1, st2]
    entry_data['value'] = [value1, value2]
    entry_data['comission'] = comissionT

def print_scenarios(scenarios):
    print('|','_-'*36,'|')
    st1 = entry_data['num_stock'][0]
    st2 = entry_data['num_stock'][1]
    for scenario in scenarios:

        p1_out = scenario[0]
        p2_out = scenario[1]

        comission1_out = get_comission(st1 * p1_out,0.06, 0.5)
        comission2_out = get_comission(st2 * p2_out, 0.0006, 4)
        comissionT_out = round(comission1_out + comission2_out,2)


        # MAke the # Stocks the Negative part:
        net1 = round( (p1_out-p1)*st1, 2)
        net2 = round( (p2_out-p2)*st2, 2)


        scenarios_df.append( [
            p1_out, 
            p2_out,
            p1_out/p2_out, # RATIO
            net1, #GAIN_1
            net2, #GAIN_2
            net1 + net2, #NET
            entry_data['comission'] + comissionT_out, #COMISSION
            net1 + net2 - (entry_data['comission'] + comissionT_out), # PnL
            round( 100 * (net1 + net2 - (entry_data['comission'] + comissionT_out)) / max(entry_data['value'][0], entry_data['value'][1]) ,2) #RET
        ])

def max_min(df, num_days = 200):
    ratio = df['ratio'].iloc[-num_days:].values

    max_ratio = round(ratio.max(),3)
    mean_ratio = round(ratio.mean(),3)
    min_ratio = round(ratio.min(),3)

    ratio_stats = {
        'max': max_ratio,
        'mean': mean_ratio,
        'min': min_ratio
    }

    #print('\nMax:\t%.2f\nMean:\t%.2f\nMin:\t%.2f' % ( max_ratio, mean_ratio,min_ratio))
    #print('\nLast:\t', round(last_ratio,2))
    
    return ratio_stats

''' Code '''
if get_data == 1 :
    df = get_prices(start_date, tickers)
    #path = '/Users/filipepessoajorge/OneDrive/X02 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Quant/Strat_Backtest/Pair_trading/%s.csv' % (tickers[0]+'_'+tickers[1])
    #df.to_csv(path)
else:
    path = '/Users/filipepessoajorge/OneDrive/X02 - Python_Developing/GitHub/Economic_data/Economic_data/BBB_Investments/Quant/Strat_Backtest/Pair_trading/%s.csv' % (tickers[0]+'_'+tickers[1])
    df = pd.read_csv(path)


df['ratio'] = df[tickers[0]]/df[tickers[1]]
print('\n', df.tail(3))

''' POSITIONS '''  # MAKE IT OPTION TO PRINT A POSITION:
#Entering Ratio:
last_ratio = df['ratio'].iloc[-1]

#Prices:
p1 = df[tickers[0]].iloc[-1]
p2 = df[tickers[1]].iloc[-1]


# Number of Stocks
st1 = int(value/p1)
st2 = round((round(last_ratio, 4) * st1),0)


#FEES:
fixed_fee_1 = init_fee_1
fixed_fee_2 = init_fee_2

'''COPY PASTE ENTRIES '''


'''END PASTE '''

#COMPILE DATA:
entry_data = {
              'num_stock': [ st1, st2], 
              'price': [ p1, p2 ],
              'fixed_fee':[ fixed_fee_1, fixed_fee_2 ]
            }


#ENTRY COSTS - 
open_position(entry_data, long_st) 
ratio_stats = max_min(df, num_days = num_days)


last_stock_2 = round(df[tickers[1]].iloc[-5],3) # To compute Ratios
scenarios = [
    [ round ( last_stock_2 * ratio_stats['max'] ,3 )  , last_stock_2 ],
    [ round ( last_stock_2 * ratio_stats['min'] ,3 ) , last_stock_2 ],
    [ round ( last_stock_2 * (ratio_stats['max'] + ratio_stats['min'])/2 ,3 ) , last_stock_2 ], #TARGET
    [ round(df[tickers[0]].iloc[-30],3), round(df[tickers[1]].iloc[-30],3) ],  # 30 days before
    [ round(df[tickers[0]].iloc[-15],3), round(df[tickers[1]].iloc[-15],3) ],  # 15 days before
    [ round(df[tickers[0]].iloc[-5],3), round(df[tickers[1]].iloc[-5],3) ]  # 5 days before
    ]

#EXTRA: 
scenarios.append([ round ( last_stock_2 * target_ratio ,3 )  , last_stock_2 ]) 
#scenarios.append([ last_stock_2 * target_ratio, last_stock_2]) 
#scenarios.append([ df[tickers[0]].iloc[-1], df[tickers[1]].iloc[-1] ]) 

# To build Table with SCENARIOS
scenarios_df = [] 
print_scenarios(scenarios)

# Compile SCEANRIOS
scenarios_df = pd.DataFrame( scenarios_df, columns = ['price_1', 'price_2', 'ratio', 'gain_1', 'gain_2', 'net_gains','comission','PnL','Return'] )
scenarios_df = scenarios_df.T
pd.options.display.float_format = '{:,.2f}'.format #Format Display
print('\n')
scenarios_df.columns = ['max_ratio','min_ratio','average','30days_ago','15days_ago','5days_ago','extra']

#Print IT
print(scenarios_df)

#Delimiter
print('|','_-'*36,'|')

''' PLOTTING '''
if long_st==1:
    print('\nRisk-Reward (Max/ Min):\t\t', round(-scenarios_df['max_ratio'].iloc[-2]/scenarios_df['min_ratio'].iloc[-2], 2) )
else:
    print('\nRisk-Reward (Min/ Max):\t\t', round(-scenarios_df['min_ratio'].iloc[-2]/scenarios_df['max_ratio'].iloc[-2], 2) )
print('For the last %i days' % num_days)

print('\nAverage Ratio: ', round(df['ratio'].mean(),3))

print('Last prices:\t', scenarios[-1])
print('\nThe End\n')


#PLOT PRICES
if plot_prices ==1:
    df[tickers[0]].plot(legend = tickers[0])
    df[tickers[1]].plot(legend = tickers[1])
    plt.show()

if plot_ratio == 1:
    df['ratio'].iloc[-num_days:].plot(title = tickers[0]+'/'+tickers[1])
    plt.show()


#CORRELATION
#df[tickers[0]].rolling(window=200).corr(other=df[tickers[1]]).plot(legend = 'Correlation')
#plt.show()

'''
# ENTRIES
# CHANGING ENTRIES



# Prices After Entry 

#EDPs
p1 = 17.58
p2 = 4.455
st1 = 15.0 
st2 = 59.0 
long_st = 0

#GALP:
p1 = 9.308
p2= 8.33
st1 = 22
st2 = 25
long_st = 1



'''