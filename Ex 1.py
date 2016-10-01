__author__ = 'student'

A = list(map(int, input().split()))
print(' '.join(map(str, A[::2])), end=" ")


print()


A = list(map(int, input().split()))
print(max(A), A.index(max(A)), end=" ")


print()


A = list(map(int, input().split()))
print(' '.join(map(str, A[::-1])), end=" ")


