import pandas as pd

# From both files in this folder: CSV
df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/df.csv')
sector_df = pd.read_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/WebScrapping/SP500/Output_csv/sector_industry.csv')

#print(sector_df)

save_nr_firms=0 #Per Sector
save_nr_firms_2=0 #Per #Firms in industry
print()

#companies
nr_firms = []

for sector in sector_df.columns:
    for industry in sector_df[sector]:
        if str(industry) != 'nan':
            filter_ = df.loc[(df['sector'] == sector) & (df['industry']==industry) ]
            nr_firms.append([sector, industry, filter_.size])

nr_firms = pd.DataFrame(nr_firms, columns=['sector', 'industry', '#Firms'])
nr_firms.sort_values(by=['#Firms'], inplace=True, ascending=False)

print(nr_firms)


#Save Output - Visualization
if save_nr_firms==1:
    with open("WebScrapping/SP500/Output_csv/nr_firms_industry.txt", 'a') as f:
        for sector in sector_df.columns:
                f.write('Sector: %s\n' % sector)
                for industry in sector_df[sector]:
                    if str(industry) !='nan':
                        filter_ = df.loc[(df['sector'] == sector) & (df['industry']==industry) ]
                        f.write('%s, %d \n' % (industry, int(filter_.size) ))
                f.write('\n\n\n')

#Save - Visualization
if save_nr_firms_2==1:
    with open("WebScrapping/SP500/Output_csv/nr_firms_industry_descending.txt", 'a') as f:
        for index, row in nr_firms.iterrows():
                f.write('%d , %s , %s\n' % (row['#Firms'], row['industry'] , row['sector'] ))

