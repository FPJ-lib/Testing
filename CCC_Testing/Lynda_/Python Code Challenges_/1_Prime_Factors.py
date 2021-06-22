#Get Prime number:
'''

get_prime_factors(360)

[2,3,3,5,7]

'''

def get_prime_numbers(N):
    factors = list()
    divisor = 2
    while (divisor <=N):
        if ( N% divisor) == 0:
            factors.append(divisor)
            N= N/divisor
        else:
            divisor += 1
    return factors

print('\n')
print(get_prime_numbers(360))
print('\n')

