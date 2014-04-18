"""
    This is a simple example of how to use the multiprocessing library in 
    Python 2.3+ with objects.  Process Pools are probably a better way
    of solving the producer consumer problem in Python, but the
    purpose of this example is to just demonstrate the basics.

    See multiprocessing.pool for more details, and an example of using Pool:
    http://goo.gl/1JuEf8
"""
import multiprocessing
import random
import math
import sys

def mrange(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

class PuffyCoinMiner(multiprocessing.Process):
    def __init__(self, out_queue, floor=10000000, ceiling=sys.maxint):
        multiprocessing.Process.__init__(self)
        self.out_queue = out_queue
        self.mined_coins = dict()
        self.ceiling = ceiling
        self.floor = floor

    def run(self):
        while True:
            number = random.randint(self.floor, self.ceiling)
            if self.is_prime(number) and number not in self.mined_coins:
                self.mined_coins[number] = True
                self.out_queue.put(number)

    def is_prime(self, n):
        ''' Takes a number in, checks if it is prime.  Shamelessly
            stolen from: https://coderwall.com/p/utwriw to save
            some time while writing this example.
        '''
        return not any(n % i == 0 for i in mrange(3, int(math.sqrt(n)) + 1, 2))
        
class PuffyCoinSeller(multiprocessing.Process):
    def __init__(self, in_queue):
        multiprocessing.Process.__init__(self)
        self.in_queue = in_queue
        self.num_mined_coins = 0

    def run(self):
        while True:
            new_prime = self.in_queue.get()
            self.num_mined_coins += 1
            price = math.log(self.num_mined_coins)
            print "New PuffyCoin #", new_prime, 
            print "price is: ${:03.2f}".format(price)

def main():
    coin_queue = multiprocessing.Queue()
    miner = PuffyCoinMiner(coin_queue)
    seller = PuffyCoinSeller(coin_queue)

    miner.start()
    seller.start()

    miner.join()
    seller.join()

if __name__ == "__main__":
    main()
