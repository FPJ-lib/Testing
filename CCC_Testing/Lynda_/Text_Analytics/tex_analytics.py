#https://www.lynda.com/Python-tutorials/Text-Analytics-Predictions-Python-Essential-Training/786421-2.html

import re
from collections import Counter
import pandas as pd

restrict_list = ['AND','THE','TO','YOU','A','IN','OF','OUR','YOUR','FOR','WILL',
                 'WE','WITH','WE','WITH','AS','BE','IS','ARE','ON','THAT','OR','AN',
                 'ALL','BY','HAVE','-','ACROSS','WHO','FROM','WHAT','THIS','LL','THROUGH',
                 'AT','S','ALSO','MAKE','NEED','BUT','IF','DO',"YOU'LL",'ONE','COMPANY','FIRM',
                 'NOT','OVER','COUNTRIES','GET','YEAR','SUMMER','WORK','ANALYST','HELP','WELL','TIME',
                 'ANALYSTS','NOMURA','MOELIS','CITI','MARKET','EQUIVALENT','CLIENT','PROGRAMME','START',
                 'BUILDING','LOOKING','APPLY','ROLE','ASSET','EXPECT','PART','MOST','THROUGHOUT','ABOUT',
                 'ANY','BACKGROUND','1','2','DEGREE','THEIR','OVERVIEW','INCLUDING','2021','HERE']

def count_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        
        
        
        print('\nTotal Words: ', len(all_words))

        word_counts = Counter()
        for word in all_words:
            if word not in restrict_list:
                word_counts[word] += 1


        #Save text to CSV
        df_ = pd.DataFrame(all_words, columns=['text'])
        df_.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Text_Analytics/all_words.csv', index=False)
        
        #Create Output
        words = pd.DataFrame(word_counts.most_common(), columns=['Words', 'Freq'])
        return words

df = count_words('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Twitter/Jobs_ads.txt')
df.to_csv('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Text_Analytics/word_list.csv', index=False)
print(df)

print('\nOver')
'''
print('\nTop20: ')
print(df[ df['Freq'] >= 6 ])
'''