import pandas as pd

#From file: download_data_wiki_sp500.py
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv')
print(df)
save_sectors=0

###########################################################################################
print('\n\n')

#All Sectors = 10:
sectors = pd.DataFrame(df['sector'].unique(), columns=['sectors'])
sectors = sectors['sectors'].tolist()
sectors.sort()
#print(sectors)

#Get Industry of each Sector:
sector_df=pd.DataFrame()

for sector in sectors:
    #print(sector, '\n')
    filtersector = df.loc[df['sector'] == sector]
    listofindustries =  filtersector['industry'].unique().tolist()
    listofindustries.sort()
    df2 = pd.DataFrame(listofindustries)

    sector_df = pd.concat([sector_df, df2], ignore_index=True, axis=1)
sector_df.columns = sectors
print('Industries per Sector: \n', sector_df.head(5))
print(sector_df)

#Save Output - Further Use
sector_df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/sector_industry.csv', index=False)

#Save Output - Visualization
if save_sectors==1:
    with open("WebScrapping/SP500/Output_csv/Sectors_Industry_table.txt", 'a') as f:
        for sector in sector_df.columns:
                f.write('Sector: %s\n' % sector)
                for industry in sector_df[sector]:
                    if str(industry) !='nan':
                        f.write('%s\n' % industry)
                f.write('\n\n\n')
