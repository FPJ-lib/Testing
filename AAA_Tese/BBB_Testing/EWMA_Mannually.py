import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

print('\nStart\n')


returns = np.random.normal(0.03/252, 0.07/(252**0.5) , 1000)
returns2 = np.random.normal(0.03/252, 0.07/(252**0.5) , 1000) / 2 + returns 



df=pd.DataFrame()
df['R1'] = returns
df['R2'] = returns2

df.cumsum().plot()
plt.show()


df2 = pd.DataFrame()
df2['Corr'] = df['R1'].rolling(window=50).corr(other = df['R2'])
df2.plot()
plt.show()

print(df2)

print('\nTHE END\n')