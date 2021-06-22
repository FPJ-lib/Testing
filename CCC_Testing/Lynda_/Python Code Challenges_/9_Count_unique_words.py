'''
Challenge:
Count the number each word occurs;
How often each occurs;


Input:
path to file:

Output:
Print message with
Total of words:
Top 20 most frequent
Number of occurences

'''

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

        words = pd.DataFrame(word_counts.most_common(), columns=['Words', 'Freq'])

        #print('\n\nTop20: \n')
        #for word in word_counts.most_common(20):
        #    print(word[0], '\t', word[1])

        return words


#Run def:
#df = count_words('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Python Code Challenges_/Romeo_Juliet.txt')

df = count_words('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Twitter/Jobs_ads.txt')

print('\nTop20: ')
print(df[ df['Freq'] >= 6 ])
