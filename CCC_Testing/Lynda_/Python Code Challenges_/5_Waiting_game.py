
'''

waiting_game()

Your target time if 4 seconds
---Press Enter to begin ----

Then Again:

Eaplsed Time:

'''

import time
import random

def waiting_game():
    target = random.randint(2,4) #Target seconds to wait
    print('\nYour target time is {} seconds'.format(target))

    input('---Press Enter To Begin--- ')
    start = time.perf_counter() #Godd for Short Term times

    input('\n...Press Enter Again after {} seconds'.format(target))
    elapsed = time.perf_counter() - start
    

    print('\nElapsed time: {0:.3f} seconds'.format(elapsed))
    if elapsed == target:
        print('Impossible Perfect Timing')
    elif elapsed < target :
        print('({0:.03f} to fast)'.format(target - elapsed))
    else:
        print('({0:.03f} to Slow)\n'.format(elapsed - target))


waiting_game()