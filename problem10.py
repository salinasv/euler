#! /usr/env python3

import math

import prime

#test_number = 2000000
#test_number = 200000
test_number = 2000000

primes = prime.get_primes_to(test_number)

#print("Got list", primes)
#print("last", primes[-1])

result = sum(primes)

print(result)

