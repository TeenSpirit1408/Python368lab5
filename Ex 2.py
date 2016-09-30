__author__ = 'student'

A = list(map(int, input().split()))
for i in range(0, len(A) - 1, 2):
    A[i], A[i+1] = A[i+1], A[i]
print(A, end=" ")


print()


A = list(map(int, input().split()))
B = [A[i-1] for i in range(len(A))]
print(B[::1], end=" ")


print()


A = list(map(int, input().split()))
for i in range(len(A)):
    if A.count(i) == 1:
        print(i, end=" ")


print()


imax = 0
k = 0
A = list(map(int, input().split()))
for i in range(len(A)):
    if A.count(i) > k:
        imax = i
print(imax, end=" ")

