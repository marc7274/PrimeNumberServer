def get_primes(lower, upper):
    numbers = set(range(upper, lower, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, upper+1, p)))
    return primes

print(get_primes(1000000,2000000))