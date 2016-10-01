A = list(map(int, input().split()))
for i in range(1, len(A), 2):
    A.insert(i, A[-1])
    A.pop(-1)
print(' '.join(map(str, A[::1])), end=" ")
