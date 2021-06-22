# Python program to generate WordCloud
# https://www.geeksforgeeks.org/generating-word-cloud-python/
 

# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 

# Reads 'Youtube04-Eminem.csv' file 
df = pd.read_csv(r"/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Text_Analytics/all_words.csv") 
print(df)
 
comment_words = '' 
stopwords = set(STOPWORDS) 

# iterate through the csv file 
for val in df['text']: 
	# typecaste each val to string 
	val = str(val) 

	# split the value 
	tokens = val.split() 

	# Converts each token into lowercase 
	for i in range(len(tokens)): 
		
		tokens[i] = tokens[i].lower() 
	comment_words += " ".join(tokens)+" "

#Test
print('Comment: ',comment_words,'\nend of text')

#Add Words to STOPWORDS
stopwords.update(['Will'])

#Create Word Cloud:
wordcloud = WordCloud(width = 600, height = 600, 
				background_color ='white', 
				stopwords = stopwords, 
				min_font_size = 10).generate(comment_words) 

# plot the WordCloud image:
plt.figure(figsize = (6, 6), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show()

print('\nOver')