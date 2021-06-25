import numpy as m
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.core.algorithms import diff
from pandas.core.frame import DataFrame 

# INPUTS
number_obs = 150
loop = 5000
sum_differences=[]

for number_loop in range(loop):
  X = m.matrix(m.random.standard_normal((6, number_obs)))  
  C = m.matrix(m.array([[ 1  , .2, .2, .2, .2, .2],
                        [.2  ,  1, .2, .2, .2, .2],
                        [.2  , .2,  1, .2, .2, .2],
                        [.2  , .2, .2,  1, .2, .2],
                        [.2  , .2, .2, .2,  1, .2],
                        [.2  , .2, .2, .2, .2,  1]
                      ]))
  U = m.linalg.cholesky(C)

  Y = U*X

  #And to test that this works:
  Y = pd.DataFrame(Y)
  Y = Y.T
  Y.columns=['1','2','3','4','5','6']
  #C = pd.DataFrame(C)

  obs_correl = Y.corr()
  difference = m.abs(C - obs_correl).sum()
  #print('DIFFERCE:\n', difference)

  #print('\nReal Correlation:\n', C)
  #print('\nObserved Correlation:\n', round(obs_correl,2))

  #print('\nSum of differences: \t', round(difference.sum(),2))
  sum_differences.append(round(difference.sum(),2))

sum_differences = pd.Series(sum_differences)
print()
print(sum_differences)
print( '\nAverage:\t', round(sum_differences.mean(),2))



'''
plt.plot(Y.cumsum())
plt.legend(Y.columns)
plt.show()
'''


print('\n\n')