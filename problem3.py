#! /usr/env python3

import math

import prime

number = 19885
#number = 13195
#number = 600851475143
step = 100
i = 1

factor = []

while (number != 1):
    print("step 1")
    primes = prime.get_primes_to(step * i)
    i = i + 1

    for i in primes:
        val = number / i

        if (val - math.floor(val)) != 0:
            continue

        number = val
        factor.append(i)


print(factor)
