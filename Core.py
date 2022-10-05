import random
import time

def rnd(lower=0, upper=5000):
    r = random.randint(lower, upper)
    time.sleep(r/1000)

def sleep_s():
    rnd(10, 50)