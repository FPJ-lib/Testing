'''
Challenge:
Generate Passwords

Inputs:
# Words in PassPhrase

Output:
String of random words, seperated by spaces
'''

import secrets

def generate_passphrase(num_words):
    with open('/Users/filipepessoajorge/OneDrive/X002 - Python_Developing/GitHub/Economic_data/Economic_data/Lynda_/Python Code Challenges_/diceware.wordlist.asc','r') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)

print('\n')
print(generate_passphrase(3))
print('\n')

print('Over')