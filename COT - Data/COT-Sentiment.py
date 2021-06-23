# https://medium.com/swlh/using-python-to-download-sentiment-data-for-financial-trading-1c44346926e2

#-m pip install --upgrade pip
'''
Error with Excel paths

Error -XRDL 

'''

import datetime
import pytz
import pandas            as pd
import numpy             as np
import zipfile, urllib.request, shutil
import matplotlib.pyplot as plt


#import os
#import openpyxl

def get_COT(url, file_name):
    
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        
    with zipfile.ZipFile(file_name) as zf:
            zf.extractall()


# Downloading and extracting COT files
get_COT('https://www.cftc.gov/files/dea/history/fut_fin_xls_2021.zip', '2021.zip')



# Renaming
#os.rename(r'C:/Users/filip/OneDrive/08 - Coding/Research/FinFutYY.xls',
#          r'C:/Users/filip/OneDrive/08 - Coding/Research//2020.xls')



data_2020 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/FinFutYY.xls')
data_2020 = data_2020[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]


print('\n\n')
#print(data_2020.columns.values)


'''
It is up to the trader to choose whether to net them so that he has only two 
time series to deal with or to keep the four series and make a deeper analysis.
Now, the above can be done for the previous years as well. I recommend 
downloading the COT values since 2006 so that you have enough history to
apply some statistical strategies (most of them are seen in the below 
link I have provided).


TO DO:
-Download All years (2006)
- compile per asset

'''

Markets_and_Exchanges = data_2020['Market_and_Exchange_Names'].unique()
print('\n\n')
print(Markets_and_Exchanges)
print('\n')


df_row = data_2020.loc[data_2020['Market_and_Exchange_Names'] == 'EURO FX - CHICAGO MERCANTILE EXCHANGE']
print(df_row)


# PRINT THE COLUMNS
list_titles = ['Pct_of_OI_Dealer_Long_All', 'Pct_of_OI_Dealer_Short_All', 'Pct_of_OI_Lev_Money_Long_All', 'Pct_of_OI_Lev_Money_Short_All']

#plot_title='Pct_of_OI_Lev_Money_Short_All'

plt.plot(df_row['Report_Date_as_MM_DD_YYYY'],df_row[list_titles] ) 
plt.legend(list_titles)
plt.show()


print('\n\n')