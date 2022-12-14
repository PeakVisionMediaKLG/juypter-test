import numpy as np
is_prime = np.ones((100,), dtype=bool)
# Cross out 0 and 1 which are not primes:
is_prime[:2] = 0
# cross out its higher multiples (sieve of Eratosthenes):
nmax = int(np.sqrt(len(is_prime)))
for i in range(2, nmax):
    is_prime[2*i::i] = False

print(np.nonzero(is_prime))
