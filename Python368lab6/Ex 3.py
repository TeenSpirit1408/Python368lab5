__author__ = 'student'
import numpy as np
import random
import matplotlib.pyplot as plt

file_input = open('/home/user/Рабочий стол/img.txt', 'r')


#1
def get_percentile(values, bucket_number):
    if bucket_number == 0:
        B = 1.0
    else:
        B = [0.0]
        for i in range(1, bucket_number):
            B.append(np.percentile(values, (100/bucket_number)*i))
    return B

#2
def get_percentile_number(value, percentiles):
    max = 0
    imax = 0
    for i in range(len(percentiles)):
        if (max <= percentiles[i]) &  (percentiles[i] <= value):
            max = percentiles[i]
            imax = i
    return imax

#3, 4
def value_equalization(value, percentiles, add_random = False):
    idx = get_percentile_number(value, percentiles)
    step = 1 / len(percentiles)
    if add_random == True:
        random_noise = random.uniform(0, (idx+1)*step  - (idx)*step)
        new_value = idx*step + random_noise
    else:
        new_value = idx*step
    return new_value

#5
def values_equalization(values, percentiles, add_random=False):
    A = []
    for i in range(len(values)):
        A.append(value_equalization(values[i], percentiles, add_random))
    return(A)

#6
k = 0
data = []
for i in range(200):
    data.append([])
    for j in range(267):
        data[i].append(k)
data1 = file_input.read().split()
for i in range(200):
    for j in range(267):
        data[i][j] = float(data1[k])
        k += 1
data = np.array(data)

#7
plt.imshow(data, cmap=plt.get_cmap('gray'))
plt.show()

#8
data = data.flatten()
plt.hist(data, bins=11)
plt.show()

#9

B = get_percentile(data, 5)
b = value_equalization(data, B, add_random=True)
data = values_equalization(data, B, add_random=True)
print(data)

plt.imshow(data, cmap=plt.get_cmap('gray'))
plt.show()
data = data.flatten()
plt.hist(data, bins=11)
plt.show()
