#https://blog.quantinsti.com/stock-market-data-analysis-python/


##### Not Good, but a sample? Fuck it delete it

# Define the ticker list
import pandas as pd
import quandl 
quandl.ApiConfig.api_key = 'QRisxrNExze-5RCysH3-'

start_date = '2020-09-01'
end_date = '2020-10-01'

tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Import pandas
data = pd.DataFrame(columns=tickers_list)

# Feth the data
for ticker in tickers_list:
    data[ticker] = quandl.get('WIKI/' + ticker, start_date=start_date, end_date=end_date)['Adj. Close']

# Print first 5 rows of the data
print(data)