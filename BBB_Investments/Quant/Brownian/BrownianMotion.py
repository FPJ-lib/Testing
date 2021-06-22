# -*- coding: utf-8 -*-
"""
@author: Sebastiao Vicente
@description: Some tests and experiments with Geometric Brownian Motion
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Formula -> dS / S = u.dt + sigma . dW

#NUMBER of Stocks
range_top=500
drift_ret = 0.12
std_ret = 0.22

higher_than = 130

number_bins = 50


plot=1


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
    processes.append(GeometricBrownianMotion( drift_ret , std_ret , 1/365 , 100))
    
for process in processes:
    #Reset tte for each process
    tte = 1
    while((tte - process.delta) > 0):
        process.step()
        tte -= process.delta


#print(processes[0].asset_prices)
for i in range(0,range_top):
    graph = plt.plot(np.arange(0, len(processes[i].asset_prices)), processes[i].asset_prices)


#print(processes[-1].asset_prices)
df2 = pd.DataFrame()
for i in range(0,range_top):
    df2[i] = processes[i].asset_prices

df = pd.DataFrame(df2.iloc[-1].to_list(), columns=['last'])

print(df)
print('average:\t\t', round(df['last'].mean(),2))

probability_loss = (df[df['last']<100].count()) / range_top
print('Loss %:\t\t\t', round(probability_loss['last']*100,2))


probability_higher = (df[df['last']>higher_than].count()) / range_top
print('Higher than ',higher_than,':\t', round(probability_higher['last']*100,2))

print('\n\n')
df.plot.hist(bins=number_bins)


if plot==1:
    plt.show()

