import pandas as pd 
import numpy as np 
import math
import matplotlib.pyplot as plt


# Formula -> dS / S = u.dt + sigma . dW

#NUMBER of Stocks
range_top=2

plot=0


class GeometricBrownianMotion:
     
    def step(self):
        dW = np.random.normal(0, math.sqrt(self.delta))
        dS = self.drift * self.delta * self.current_price + self.volatility * self.current_price * dW
        self.asset_prices.append(self.current_price + dS)
        self.current_price = self.current_price + dS
        
    def __init__(self, drift, vol, delta_t, initial_price):
        self.drift = drift
        self.volatility = vol
        self.delta = delta_t
        self.current_price = initial_price
        self.asset_prices = [initial_price]
        


# Sample paths list for underlying asset (100) -> Could just be 1
# Chose 100 for simulation purposes
        
processes = []
for i in range(0, range_top):
    processes.append(GeometricBrownianMotion( .15 , .17 , 1/365 , 200))
    
for process in processes:
    #Reset tte for each process
    tte = 1
    while((tte - process.delta) > 0):
        process.step()
        tte -= process.delta


#print(processes[0].asset_prices)
#for i in range(0,range_top):
#    graph = plt.plot(np.arange(0, len(processes[i].asset_prices)), processes[i].asset_prices)

if plot==1:
    plt.show()

'''____________________ END CLASS PART ____________________________________ '''
##### GET VARIANCES:


#Build Dataset
df = pd.DataFrame( )
df['A1'] = processes[0].asset_prices
df['A2'] = processes[1].asset_prices


# Returns
df = np.log(df/df.shift(1)) 
#print(df)


df['A1_ret^2'] = df['A1'] ** 2
df['A2_ret^2'] = df['A2'] ** 2

konstant = 0.94

def get_EWMA(df, column = 'A1_ret^2'):
    EWMA = []
    for row in range(len(df) + 1 ):
        if row==0:
            EWMA.append(0)
        elif row==1:
            vol = df[column].iloc[row]
            EWMA.append( vol )
        else:
            vol = EWMA[-1] * konstant + (1-konstant)*(df[column].iloc[row-1])
            EWMA.append( vol )
    return EWMA


def get_EWMA_cov(df, columns = ['A1_ret^2','A2_ret^2']):
    EWMA_cov = []
    for row in range(len(df) + 1 ):
        if row==0:
            EWMA_cov.append(0)
        elif row==1:
            cov = ( df[columns[0]].iloc[row] )* ( df[columns[1]].iloc[row] )
            EWMA_cov.append( cov )
        else:
            cov = EWMA_cov[-1] * konstant + (1-konstant)*( ( df[columns[0]].iloc[row-1] )* ( df[columns[1]].iloc[row-1] ) )
            EWMA_cov.append( cov )
    return EWMA_cov


df2 = pd.DataFrame()
df2['EWMA_A1'] = get_EWMA(df, 'A1_ret^2')
df2['EWMA_A1'] = ( df2['EWMA_A1'] ** 0.5 ) * (252**0.5)


df2['EWMA_A2'] = get_EWMA(df, 'A2_ret^2')
df2['EWMA_A2'] = ( df2['EWMA_A2'] ** 0.5 ) * (252**0.5)

df2['Real_std'] = 0.17

df2['Cov'] = get_EWMA_cov(df)
df2['Cov'] =  252 * df2['Cov'] / ( df2['EWMA_A1'] * df2['EWMA_A2'] )

print(df2)

# SHIT IS WRONG!

#df2.plot()
df2['Cov'].plot()
plt.show()

print(df)



