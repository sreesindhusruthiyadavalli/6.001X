def genPrimes():
    primes = []
    x = 1
    while True:
        x = x + 1
        for y in primes:
            if (x % y) == 0:
                break
        else:
            primes.append(x)
            yield x
            
