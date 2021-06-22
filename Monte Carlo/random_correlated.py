import numpy as m
import pandas as pd 

# INPUTS
number_obs = 500

X = m.matrix(m.random.standard_normal((5, number_obs)))  
C = m.matrix(m.array([[1  , .2, .2, .2, .2],
                      [.2 , 1., .3, .3, .3],
                      [.2 , .3, 1., .3, .3],
                      [.2 , .3, .3, 1., -.5],
                      [.2 , .3, .3, -.5, 1.],
                    ]))
U = m.linalg.cholesky(C)

Y = U*X

#And to test that this works:
Y = pd.DataFrame(Y)
Y = Y.T
C = pd.DataFrame(C)

print('\nReal Correlation:\n', C)
print('\nObserved Correlation:\n', round(Y.corr(),2))

print('\n\n')