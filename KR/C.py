__author__ = 'student'


x = int(input())
A = []
A = list(map(int, input().split()))
min1 = 10000000
max1 = -10000000
i1 = 0
i2 = 0
if x == len(A):
    for i in range(len(A)):
        if abs(A[i]) % 2 == 0 and A[i] < min1:
            min1 = A[i]
            i1 = i
    for i in range(len(A)):
        if abs(A[i]) % 2 == 1 and A[i] > max1:
            max1 = A[i]
            i2 = i
    if min1 != 10000000 and max1 != -10000000:
        A[i1], A[i2] = A[i2], A[i1]
print(*A)
