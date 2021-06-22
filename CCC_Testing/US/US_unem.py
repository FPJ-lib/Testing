#https://towardsdatascience.com/dissecting-unemployment-data-with-python-and-quandl-4d6d5d0fcdcd

import pandas as pd
import quandl
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

quandl.ApiConfig.api_key = 'QRisxrNExze-5RCysH3-'


df = quandl.get(["FRED/UNRATE", "FRED/LNS14000003", "FRED/LNS14000006", "FRED/LNS14000009", "FRED/LNU04032183"],trim_start="2000-1-1", trim_end="2022-05-01", collapse = 'monthly')
df.columns = ['Unemployment', 'Unemp_White', 'Unemp_Black', 'Unemp_Hispanic','Unemp_Asian']
print(df)


cols = [col for col in df.columns]
fig, ax = plt.subplots(1, 1, figsize=(8,5))
plt.style.use('fivethirtyeight')


for c in cols:
    ax.plot(c, linewidth=2, data=df)
    ax.set_title('Unemployment Rate by Race')
    plt.xlabel('Year')
    plt.ylabel('Percent')
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels,loc='upper left', prop={"size":10})
plt.show()


#GENDER
df = quandl.get(["FRED/LNS14000001", "FRED/LNS14000002"], trim_start="2000-1-1", trim_end="2020-05-01", collapse = 'monthly')
df.columns = ['Unemp_Men', 'Unemp_Women']
print(df)

#RACE & GENDER
df = quandl.get(["FRED/LNS14000028", "FRED/LNS14000029", "FRED/LNS14000031", "FRED/LNS14000032", "FRED/LNU04000034", "FRED/LNU04000035"],trim_start="2000-1-1", trim_end="2020-05-01", collapse = 'monthly')
df.columns = ['Unemp_White_Men', 'Unemp_White_Women', 'Unemp_Black_Men', 'Unemp_Black_Women', 'Unemp_Hispanic_Men', 'Unemp_Hispanic_Women']
print(df)

# By AGE
df = quandl.get(["FRED/LNS14000036", "FRED/LNS14000089", "FRED/LNS14000091","FRED/LNS14000093", "FRED/LNS14024230"],trim_start="2000-1-1", trim_end="2020-05-01", collapse = 'monthly')
df.columns = ['20-24', '25-34', '35-44', '45-54', '55 and up']
print(df)

#By Education
df = quandl.get(["FRED/LNS14027659", "FRED/LNS14027660", "FRED/LNS14027662", "FRED/CGMD25O", "FRED/CGDD25O"],trim_start="2000-1-1", trim_end="2020-05-01", collapse = 'monthly')
df.columns = ['Unemp (>25, less than HS)', 'Unemp (>25, HS)', 'Unemp (>25, College)', 'Unemp (>25, Master)', 'Unemp (>25, Doctoral)']
print(df)

