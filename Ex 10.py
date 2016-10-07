__author__ = 'student'

N = int(input())
A = [1]
B = [1, 1]
if N == 1:
    print(*A)
else:
    for j in range(N):
        for i in range(1, len(A)):
            B.insert(i, A[i-1]+A[i])
        A = B
        B = [1, 1]
    print(*A)

