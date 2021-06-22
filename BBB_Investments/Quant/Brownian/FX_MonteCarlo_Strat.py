
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from random import *

number_scenarios = 1 + 10
number_trades = 20

win_ratio = 0.32
risk_reward = 2.8
risk_per_trade = .08

start = 300

print('\nBreak-even Win-ratio:\t', round(100/(risk_reward+1),2))
print('Win-Ratio:\t\t', round(win_ratio*100,2))



# Create an empty list
accounts = []
for i in range(number_scenarios):
    # In each iteration, add an empty list to the main list
    accounts.append([])
    accounts[i].append(start)



for account_number in range(number_scenarios):
    for i in range(number_trades):
        if random() < win_ratio:
            append = accounts[account_number][-1]*(1+risk_per_trade*risk_reward)
            accounts[account_number].append(round(append,2))
        else:
            append = accounts[account_number][-1]*(1-risk_per_trade)
            accounts[account_number].append(round(append,2))

print('\n\n')

#Data Frame
df = pd.DataFrame(accounts)
print(df.T)

print('\nMean:\t  ', round(df[number_trades].mean(),2))
print('Max:\t', df.max().max())
print('Min:\t   ', df.min().min())


#SAVE DF
df = df.T
df.to_csv('C:/Users/filip/OneDrive/08 - Coding/Research/BBB_Investments/Quant/Brownian/MonteCarlo_FX.csv', index=False)


print()