__author__ = 'student'

A = list(map(int, input().split()))
for i in range(0, len(A), 1):
    A[i:i+1] = [A[-i], A[i+1]]
    b = A.pop(-i)
print(A[::1], end=" ")