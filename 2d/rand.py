import os
import random

open("data.txt", "w").write("%i\n" %random.randint(0,10))

while True:
    open("data.txt", "a").write("%i\n" %random.randint(0,10))