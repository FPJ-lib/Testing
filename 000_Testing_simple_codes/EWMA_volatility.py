import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

plot_ = 1
rolling_window = 22
'''
So Far it is Working:

---> Only one Asset.
---> Simple


- Missing another Asset to compute Covariance & Correlation. 
---> Hardest Part


Why this ?
- When Covariances And overal Correlation ---> 1.0
---> LTCM Case. Respond to unstable market environments



'''

price = pd.DataFrame([10,11,13,9,12,11,14,15,12,19,16,14,17,18,17,15,14,18,19,20,23,21,19,21,20,21,23,25,21,23,24,25,28,20,30,39,37,33,31,29,28,25,25,25,25,25,25,25,25,26,27,28,29,32,35,31,29,30,29,28,29,20,29,28,26,28,20,30,31,32,35,34,33,33,37,32,31,29,26,30,37,35], columns = ['price'])


#MAKE IT returnsURNS:
price['returns'] = np.log(price['price']/price['price'].shift(1))
price.dropna(inplace=True)
#print(price)


#SAVE returnsURNS:
returns = price['returns'].values.tolist()



def square(list):
    return [i ** 2 for i in list]


ewma = []
def compute_ewma(list_returns):
    returns_squared = square(list_returns)

    print('\n')
    lambda_k = 0.94
    for row in range(len(list_returns)):
        #print(list_returns[row], '\t\t', returns_squared[row])

        if row == 0:
            print('1st row - Skipped')
        elif row == 1:
            value_append = returns_squared[row-1]
            ewma.append(value_append)
        else:
            decay = lambda_k * ewma[-1]
            added = (1-lambda_k) * (returns_squared[row-1])
            ewma.append(decay + added)
    return ewma

ewma = compute_ewma(returns)


# COUNT - EWMA DATA:
counter = 0
for i in ewma:
    #print(i)
    counter += 1
print('\nEWMA Counter:\t\t', counter)


''' Rolling Volatility '''
# ROLLING VOLATILITY:
price['vol'] = price['returns'].rolling(window=rolling_window).var()
price['vol'].dropna(inplace=True)

#COUNT - ROLLING Volatility:
number_vol = price['vol'].count()
print('Rolling Counter:\t',number_vol)
print('Total Returns:\t\t', price['returns'].count())


'''Compare RESULTS '''
df = pd.DataFrame(ewma[-number_vol:], columns=['ewma'])
df['rolling'] = price['vol'].iloc[-number_vol:].tolist()
#df['cumulative'] = returns[-number_vol:]
#df['cumulative'] = df['cumulative']/4

print('\n')
print(df.tail(number_vol))


# PLotting GRAPH
if plot_ == 1:
    df.plot()
    plt.show()


#print('\n')