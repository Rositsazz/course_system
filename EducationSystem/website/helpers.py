def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n - 1)


def fibonacci(n, f1=0, f2=1):
    if n == 0:
        return f2
    return fibonacci(n - 1, f2, f1 + f2)


def first_N_primes(n):
    def gen_numbers():
        for x in range(3, 100000000000):
            yield x

    number_gen = gen_numbers()

    def first_primes(n):
        if n == 1:
            return [2]
        last_primes = first_primes(n - 1)
        x = next(number_gen)
        prime_check = True
        while prime_check:
            prime_check = False
            for prime in last_primes:
                if x % prime == 0:
                    x = next(number_gen)
                    prime_check = True
                    break
        return last_primes + [x]
    return first_primes(n)
