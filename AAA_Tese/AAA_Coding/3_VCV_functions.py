import pandas as pd 
import numpy as np
import math 
import matplotlib.pyplot as plt 


def get_MCR(w, VCV, returns, std_p):
    number_rows = VCV.shape[0] 
    MCR = [] 
    for i in range(number_rows):
        MCR.append( (([row[i] for row in VCV] * np.matrix(w).T) / std_p ) * w[i]) # Missing Multiply by W_i
    MCR = np.concatenate((MCR[0] , MCR[1], MCR[2]))
    return MCR


def get_RiskParity_weights(returns):
    
    VCV = returns.cov().values * 252
    print('\nVCV_Covariance Values')
    print(VCV)

    print('Variances:\n')
    Var = returns.std() * math.sqrt(252)
    print( Var )
    
    #Change it to an Optimization Process:
    w = [0.180,
         0.680, 
         0.14
        ]

    std_p = math.sqrt(np.matrix(w) * VCV * np.matrix(w).T)
    MCR = get_MCR(w, VCV, returns, std_p)
    MCR = (MCR/MCR.sum()) * 100
    print('\nSTD_Portfolio:\n', std_p)
    
    print('\n\nMCR:\n', MCR)
    return w, std_p, MCR


#Returns
df_returns = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df_returns.csv')
df_returns = df_returns.set_index('Date')
print(df_returns)

w, std_p, MCR = get_RiskParity_weights(df_returns)

print('\n\nWeights\n%s, \n\nSTD_Portfolio\n%f,\n\nMCR\n%s' % (w, std_p, MCR))


#Cumulative Returns
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
df = df.set_index('Date')
print('\n\n####\n:',df)

df = df * np.array( w )
print(df)

df['RP'] = df.sum(axis=1)
df['RP'] = df['RP'] / df['RP'].iloc[0]
print(df)

