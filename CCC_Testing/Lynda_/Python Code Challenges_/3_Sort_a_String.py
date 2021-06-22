'''

Sort the words in a string;

String of waords sorted alphabetically

'''

check = 'banana ORANGE apple'

def sort_words(input):
    words = input.split()
    print('\nSPLIT: ',words)
    

    words = [w.lower() + w for w in words]
    print(words)
    words.sort()

    words = [w[len(w)//2:] for w in words]

    return ' '.join(words)

print('\n')
print(sort_words(check))
print('\n')
    


print('3/5 = ', 3/5)
print('3//5 = ', 3//5) # Modular part: Nice