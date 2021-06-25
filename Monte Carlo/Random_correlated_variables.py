import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from pandas.core.algorithms import diff 

'''
TO-DO:
-How to create Positive Definite Values
-What a Positive Definite MAtrix Is



'''


# Objective: Create a Correlation Matrix
number_of_assets = 6
correlation_per_asset = np.matrix(np.random.rand(1, number_of_assets)*2 -1 ) 
correlation_per_asset = correlation_per_asset.round(3)


#Check the Correlation Matrix
print(pd.DataFrame(correlation_per_asset))
print()

def get_correlation_matrix(correl=correlation_per_asset, size_matrix = number_of_assets):
  matrix_list =[]

  for row in range(number_of_assets):
    #Clean Next Row
    list_row=[]

    for col in range(number_of_assets):
      if row == col:
        list_row.append(1.00)
      elif row < col :
        list_row.append(correl[0, col])
      else:
        # Already computed
        list_row.append(matrix_list[col][row])

    matrix_list.append(list_row)

  Correl_Matrix = np.matrix(matrix_list)
  return Correl_Matrix


Correl_Matrix = get_correlation_matrix()
print(pd.DataFrame(Correl_Matrix))

print('Up is result')
print('\n\n')


#Code below Works
##################################################################################

# INPUTS
number_obs = 20

X = np.matrix(np.random.standard_normal((number_of_assets, number_obs)))  
C = Correl_Matrix
U = np.linalg.cholesky(C)
Y = U*X

#And to test that this works:
Y = pd.DataFrame(Y)
Y = Y.T
Y.columns=[i for i in range(number_of_assets)]
C = pd.DataFrame(C)

C_obs = round(Y.corr(),2)
print('\nReal Correlation:\n', C)
print('\nObserved Correlation:\n', C_obs)

diference = C_obs - C
print('\nDiference')
print(diference)

#print('Sum differences:\t', diference.sum()-number_of_assets)

'''
plt.plot(Y.cumsum())
plt.legend(Y.columns)
plt.show()
'''




print('\n\n')