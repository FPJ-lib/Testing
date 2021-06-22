# String Read the same forwards and backwards

#input: String:
#Output: Boolean

import re

check = "Go hang a salami - I'm a lasagna hog."

def is_palindrome(phrase):
    
    print(phrase)

    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    print(forwards)

    backwards = forwards[::-1]
    print(backwards)
    return forwards == backwards


print('\n')
print(is_palindrome(check))
print('\n')
    

