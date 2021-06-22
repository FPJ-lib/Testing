import numpy as np    
import pandas as pd

'''
https://stackoverflow.com/questions/20626994/how-to-calculate-the-inverse-of-the-normal-cumulative-distribution-function-in-p
NORMSINV


'''

print()
print()
n_obs = 100000
means = [0, 0, 0]
sds = [ 1, 1, 1] # standard deviations 

# generating random independent variables 
observations = np.vstack([ np.random.normal(loc=mean, scale=sd, size=n_obs)
                   for mean, sd in zip(means, sds)])  # observations, a row per variable

df = pd.DataFrame(observations)
df = df.T
print(df)
print()


cor_matrix = np.array([[1.0, 0.4, -0.1],
                       [0.4, 1.0, 0.05],
                       [-0.1, 0.05, 1.0]])

L = np.linalg.cholesky(cor_matrix)

print(pd.DataFrame(cor_matrix))
print()
print()
#print(np.corrcoef(L.dot(observations))) 


# - MATRIX NOTATION:
random_matrix = np.matrix(df)
#print(random_matrix)

correlated_returns = random_matrix*cor_matrix


print()
#print('SIZE:\t', random_matrix.shape)

print()
#print('Correlated returns:\t', correlated_returns)


print(pd.DataFrame(correlated_returns).corr())


print()
print()