import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import math



df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/AAA_Tese/Data_/df.csv')
df = df.set_index('Date')
print(df)

df_returns = df.pct_change().dropna()
print(df_returns)

tickers = df.columns
print(tickers, '\n')


VarCovar = df_returns.cov() * 252
VarCovar = VarCovar.values
print(VarCovar, '\n')


''' COMPUTE MINIMUM '''
from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn,0, method='BFGS')

print(mymin)