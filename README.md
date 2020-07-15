# hello-world
Python blocks storage

t0 = time.time() #compute the time required to test the integers
for n in range(1, 100000):
    is_prime_v1(n)
t1 = time.time()
print("Time required:  ", t1 - t0)


for n in range(1, 100):
    print(n, is_prime_v1(n))

import time
def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False #1 is not a prime number
    for d in range(2, n): #loop over all numbers from 2 to n - 1
        if n % d == 0: #like MOD
            return False
        return True #this ends the loop
