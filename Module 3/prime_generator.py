def is_prime(number):
    divisors = [i for i in range(1, number) if (number % i) == 0]

    if len(divisors) > 1:
        return False

    return True

def generate_primes(number_to_generate):
    count = 0
    current_number = 2

    while count < number_to_generate:
        if is_prime(current_number):
            count += 1
            yield current_number

        current_number += 1

if __name__ == '__main__':
    for prime in generate_primes(1000):
        # do something interesting with this prime
        print "{0} is prime".format(prime)
