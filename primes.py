"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    n = 2
    i=0
    while i < number_of_primes:
        prime = True
        for j in range(2, n) :
            if n % j == 0:
                prime = False

        if prime:
            list.append (n)
            i += 1

        n += 1
    return list