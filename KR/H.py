__author__ = 'student'


def f(a, b):
    k = 0
    for i in range(1, (min(a, b)+1)):
        if a % i == 0 and b % i == 0:
            k += 1
    if k == 1:
        return True
    else:
        return False

a = int(input())
A = []
k = 0
l = 0
for i in range(a):
    a, b = list(map(int, input().split()))
    if f(a, b) == True:
        A.append(a)
        A.append(b)
        l += 1

B = []
for i in range(l):
    B.append([])
    for j in range(2):
        B[i].append(A[k])
        k += 1
for i in range(l):
    print(*B[i])
