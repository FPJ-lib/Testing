# https://medium.com/swlh/using-python-to-download-sentiment-data-for-financial-trading-1c44346926e2

'''
Error with Excel paths

Error -XRDL 

'''

import datetime
import pytz
import pandas            as pd
import numpy             as np
import zipfile, urllib.request, shutil
import os
#import openpyxl

def get_COT(url, file_name):
    
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        
    with zipfile.ZipFile(file_name) as zf:
            zf.extractall()


# Downloading and extracting COT files
get_COT('https://www.cftc.gov/files/dea/history/fut_fin_xls_2020.zip', '2020.zip')



# Renaming
os.rename(r'C:/Users/filip/OneDrive/08 - Coding/Research/FinFutYY.xls',
          r'C:/Users/filip/OneDrive/08 - Coding/Research//2020.xls')



data_2020 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/2020.xls', engine='openpyxl')
data_2020 = data_2020[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]


print('\n\n')
print(data_2020)





print('\n\n')