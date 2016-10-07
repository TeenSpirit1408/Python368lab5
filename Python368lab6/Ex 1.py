__author__ = 'student'


import random
import matplotlib.pyplot as plt

random.seed(0)
n = 100
values = [random.normalvariate(0, 1) for i in range(n)]
plt.subplot(221)
plt.hist(values, bins=100)



random.seed(0)
n = 1000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.subplot(222)
plt.hist(values, bins=100)



random.seed(0)
n = 10000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.subplot(223)
plt.hist(values, bins=100)




random.seed(0)
n = 100000
values = [random.normalvariate(0, 1) for i in range(n)]
plt.subplot(224)
plt.hist(values, bins=100)


plt.show()
