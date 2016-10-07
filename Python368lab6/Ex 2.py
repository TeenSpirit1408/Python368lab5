__author__ = 'student'


import random
import matplotlib.pyplot as plt

def f(x):
    if -2 <= x <= 2:
        y = -x**2 + 4
    else:
        y = 0
    return y

n = int(input())
Y = [f(random.uniform(-3, 3)) for i in range(n)]

print(sum(Y)*6/n)


