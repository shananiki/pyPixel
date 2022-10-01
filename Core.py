import random
import time

def rnd(lower=0, upper=5000):
    r = random.randint(lower, upper)
    time.sleep(r/1000)