# Python program to generate WordCloud
# https://www.geeksforgeeks.org/generating-word-cloud-python/
 

 
import re
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS 


stopwords = ['AND','THE','TO','YOU','A','IN','OF','OUR','YOUR','FOR','WILL',
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

        '''
        word_counts = Counter()
        for word in all_words:
            if word not in stopwords:
                word_counts[word] += 1
        
        words = pd.DataFrame(word_counts.most_common(), columns=['Words', 'Freq'])
        '''
        print(all_words)
        return all_words

df = count_words('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Twitter/Jobs_ads.txt')
print(df)

print('\n\n\nTESTE:\n', df)

wordcloud = WordCloud(width = 600, height = 600, 
                      background_color ='white', 
                      stopwords = stopwords, 
                      min_font_size = 10).generate(df) 

print('TEST\n\n\n\n2####\n\n\n')

# plot the WordCloud image					 
plt.figure(figsize = (6, 6), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()

print('\nOver')