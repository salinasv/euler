import math

def is_prime(number, primes = None):
    if primes == None:
        limit = math.floor(math.sqrt(number))

        primes = get_primes_to(limit)

    for i in primes:
        val = number / i

        #test for integer
        test = val - math.floor(val)

        if (test == 0):
            return False

    return True

def simple_sieve(limit):
    p = 2
    primes = [p]

    # Exclude 2 and every even number
    lst = list(range(3, limit, 2))

    while (1):
        mark = list()

        for i in lst:
            #print(i)

            val = (i / p)
            test = val - round(val)

            if (test == 0):
                lst.remove(i)

        if len(lst) == 0:
            return primes


        p = lst[0]
        primes.append(p)
        #print(primes)
        lst.remove(primes[-1])

def sieve_atkin(limit):
    prime_list = [2,3]

    # Just lets be safe
    if (limit <= 5):
        return prime_list

    lst = list(range(1, limit))
    # Initialize the sieve
    prime = [True] * 5 + [False] * (limit - 5)

    sqrt = math.floor(math.sqrt(limit))
    #sqrt = round(math.sqrt(limit))

    # Put in candidate primes:
    for x in range(1,sqrt+1):
        for y in range(1, sqrt+1):
            n = 4 * (x**2) + y**2

            mod = n % 12
            if (n <= limit) and (( mod == 1) or (mod == 5)):
                prime[n] = not prime[n]

            n = 3 * x**2 + y**2
            if (n <= limit and (n%12 == 7)):
                prime[n] = not prime[n]

            n = 3 * x**2 - y**2
            if ((x > y) and (n <= limit) and (n%12 == 11)):
                prime[n] = not prime[n]

    for n in range(5, sqrt):
        if (prime[n]):
            mul = 1
            while True:
                eliminate = mul * n ** 2
                if eliminate >= limit:
                    break
                prime[eliminate] = False
                mul = mul + 1

    # Sum was added for Problem7
    #sum = 2
    for n in range(5,limit):
        if(prime[n]):
            prime_list.append(n)
            #sum = sum + 1
            #print(sum, n)
            #if (sum == 10002):
                #return(prime_list)

    return prime_list


def get_primes_to(limit):
    #return sieve_atkin(limit)
    return simple_sieve(limit)

def get_factor(number, primes = None):
    step = 100
    i = 1

    factor = []

    while (number != 1):
        print("step 1")
        if (primes == None):
            primes = prime.get_primes_to(step * i)
        i = i + 1

        for i in primes:
            val = number / i

            if (val - math.floor(val)) != 0:
                continue

            number = val
            factor.append(i)

    return factor

def test():
    a = get_primes_to(120)

    print("RESULT: ", a)
