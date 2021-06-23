import pandas as pd
import matplotlib.pyplot as plt





data_2016 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/COT - Data/Downloaded_Data/2006_2016.xls')
data_2017 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/COT - Data/Downloaded_Data/2017.xls')
data_2018 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/COT - Data/Downloaded_Data/2018.xls')
data_2019 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/COT - Data/Downloaded_Data/2019.xls')
data_2020 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/COT - Data/Downloaded_Data/2020.xls')
data_2021 = pd.read_excel('C:/Users/filip/OneDrive/08 - Coding/Research/COT - Data/Downloaded_Data/2021.xls')


data_2016 = data_2016[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]

data_2017 = data_2017[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]

data_2018 = data_2018[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]

data_2019 = data_2019[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]                                

data_2020 = data_2020[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]

data_2021 = data_2021[['Market_and_Exchange_Names', 
                                 'Report_Date_as_MM_DD_YYYY',
                                 'Pct_of_OI_Dealer_Long_All',
                                 'Pct_of_OI_Dealer_Short_All',
                                 'Pct_of_OI_Lev_Money_Long_All',
                                 'Pct_of_OI_Lev_Money_Short_All',]]


print('\n\n')
print(data_2016)



'''
--------------------------------------------------------------READ-READ--------
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
#print(Markets_and_Exchanges)
print('\n')


df_row = data_2016.loc[data_2016['Market_and_Exchange_Names'] == 'EURO FX - CHICAGO MERCANTILE EXCHANGE']
#print(df_row)


# PRINT THE COLUMNS
list_titles = ['Pct_of_OI_Dealer_Long_All', 'Pct_of_OI_Dealer_Short_All', 'Pct_of_OI_Lev_Money_Long_All', 'Pct_of_OI_Lev_Money_Short_All']

plot_title='Pct_of_OI_Lev_Money_Short_All'

plt.plot(df_row['Report_Date_as_MM_DD_YYYY'],df_row[list_titles] ) 
plt.legend(list_titles)
plt.show()




print('\n\n')