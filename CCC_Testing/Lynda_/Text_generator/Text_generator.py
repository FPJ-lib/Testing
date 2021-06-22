#https://www.analyticsvidhya.com/blog/2018/03/text-generation-using-python-nlp/

#GITHUB
#https://github.com/pranjal52/text_generators

import numpy as np
import pandas as pd

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

print()

#Load Data
text=(open('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Text_generator/poema1.txt').read())
text=text.lower()

#Word Mappings:
characters = sorted(list(set(text)))

n_to_char = {n:char for n, char in enumerate(characters)}
char_to_n = {char:n for n, char in enumerate(characters)}


#Data Pre-processing:
X = []
Y = []
length = len(text)
seq_length = 100

for i in range(0, length-seq_length, 1):
    sequence = text[i:i + seq_length]
    label =text[i + seq_length]
    X.append([char_to_n[char] for char in sequence])
    Y.append(char_to_n[label])


X_modified = np.reshape(X, (len(X), seq_length, 1))
X_modified = X_modified / float(len(characters))
Y_modified = np_utils.to_categorical(Y)


#Baseline Model:
model = Sequential()
model.add(LSTM(400, input_shape=(X_modified.shape[1], X_modified.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400))
model.add(Dropout(0.2))
model.add(Dense(Y_modified.shape[1], activation='softmax'))

print('\nStep1:\n')
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(X_modified, Y_modified, epochs=1, batch_size=100) #Layers

model.save_weights('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Text_generator/text_generator_400_0.2_400_0.2_baseline.h5')
model.load_weights('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Text_generator/text_generator_400_0.2_400_0.2_baseline.h5')





print('\nStep2:\n')

#Generating Text:
string_mapped = X[99]
full_string = [n_to_char[value] for value in string_mapped]
# generating characters
for i in range(400):
    x = np.reshape(string_mapped,(1,len(string_mapped), 1))
    x = x / float(len(characters))

    pred_index = np.argmax(model.predict(x, verbose=0))
    seq = [n_to_char[value] for value in string_mapped]
    full_string.append(n_to_char[pred_index])

    string_mapped.append(pred_index)
    string_mapped = string_mapped[1:len(string_mapped)]

print()

#combining text
txt=""
for char in full_string:
    txt = txt+char
print(txt)