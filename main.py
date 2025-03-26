# Graeme M
# Lists
# March 26/25
# This code creates 100 random numbers and prints the average
import random
import math
def list(): return random.randint(1,100)
lelist = [list() for i in range (100)]
print(lelist)
average = sum(lelist) / 100
print(average)