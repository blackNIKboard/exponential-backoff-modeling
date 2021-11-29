import math
import random


def get_poisson(lamb):
    check = math.exp(-lamb)
    p = 1.0
    k = 0

    while p > check:
        k += 1
        p *= random.uniform(0, 1)

    return k - 1


def poisson(lamb, size) -> list:
    return [get_poisson(lamb) for _ in range(size)]
