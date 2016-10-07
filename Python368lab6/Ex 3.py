__author__ = 'student'
import numpy as np

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
        if max <= percentiles[i] <= value:
            max = percentiles[i]
            imax = i
    return imax


#3
def value_equalization(value, percentiles):
    idx = get_percentile_number(value, percentiles)
    step = 1/len(percentiles)
    new_value = idx*step
    return new_value






A = [3, 4, 1, 2, 5, 6, 7, 8, 9, 10]
n = int(input())
B = get_percentile(A, n)
print(B)

k = float(input())
print(get_percentile_number(k, B))

l = float(input())
print(value_equalization(l, B))
