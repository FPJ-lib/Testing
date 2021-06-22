import numpy as np    
import pandas as pd



print()
print()
n_obs = 10000
means = [0.05, 0.08, 0.12]
sds = [ 0.15, 0.22, 0.3] # standard deviations 

# generating random independent variables 
observations = np.vstack([np.random.normal(loc=mean, scale=sd, size=n_obs)
                   for mean, sd in zip(means, sds)])  # observations, a row per variable

df = pd.DataFrame(observations)
df = df.T
print(df)
print('\n\n')


cor_matrix = np.array([[1.0, 0.8, -0.1],
                       [0.8, 1.0, 0.4],
                       [-0.1, 0.4, 1.0]])

L = np.linalg.cholesky(cor_matrix)

print(cor_matrix)
print()
print()
print(np.corrcoef(L.dot(observations))) 





print()
print()