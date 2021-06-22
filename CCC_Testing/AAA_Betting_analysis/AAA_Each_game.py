import numpy as np


#Gil Vicente, Rio Ave: 03:33

#Write ODDS
odds = [
    3.1,
    3.15,
    2.45
]
odds = np.array(odds)

#Odds:
print('\nOdds')
print(odds)
print('\n')

# Implied Probability:
odds_implied = np.round(100/odds,2)
print('\nProbabilities:\n',odds_implied)

#Sum probabilities:
odds_implied_sum = round(odds_implied.sum(),2)
print('\n\nSum Probabilities: \t', odds_implied_sum)
print('You will always pay more because odds are too low.')

'''
-----Defined:
Past season - 3 Seasons:

Win - Draw - Loss 
Home - Away

For the 18 Teams


-----Relative:
-How last game win affects next game:

-Autocorrelation




'''

print('\n\n')