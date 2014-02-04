import random
import cProfile

def generate_ints_comprehension():
    return [random.randint(0,10) for i in range(0, 1000000*10)]


def generate_ints():
    l1 = list()
    for i in range(0, 1000000*10):
        l1.append(random.randint(0, 10))

    return l1


def higher_than_comprehension(stuff):
    return [i for i in stuff if i > 8]

def higher_than(stuff):
    result = list()
    for i in stuff:
        if i > 8:
            result.append(i)

    return result

def main():
    result = generate_ints_comprehension()
    result = generate_ints()
    higher_than_comprehension(result)
    higher_than(result)

cProfile.run("main()")
