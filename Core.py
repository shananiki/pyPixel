import random
import time


def rnd(lower: int = 0, upper: int = 5000):
    r = random.randint(lower, upper)
    time.sleep(r / 1000)

def sleep_l():
    rnd(2000, 6000)

def sleep_s():
    rnd(10, 50)
