# https://stackoverflow.com/questions/33017564/plotting-treasury-yield-curve-how-to-overlay-two-yield-curves-using-matplotlib

#NELSON SIEGEL AND SHIT
# https://abhyankar-ameya.medium.com/yield-curve-analytics-with-python-e9254516831c


import matplotlib.pyplot as plt
import pandas as pd
import quandl as ql

ql.ApiConfig.api_key = 'QRisxrNExze-5RCysH3-'

number_of_days_ago = 30

yield_ = ql.get("USTREASURY/YIELD")

print('YIELDS:\n', yield_)

today = yield_.iloc[-1,:]
month_ago = yield_.iloc[-number_of_days_ago,:]

df = pd.concat([today, month_ago], axis=1)
df.columns = ['today', 'month_ago']

print(df)


df.plot(style={'today': 'ro-', 'month_ago': 'bx--'},
        title='Treasury Yield Curve, %')


#yield_['10 YR'].plot(title = '10 Yr Yield Curve')
#(yield_['10 YR']- yield_['2 YR']).plot(title='10YR - 2YR')
plt.show()

print()