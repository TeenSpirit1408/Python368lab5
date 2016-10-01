k, n = map(int, input().split())
A = []
for i in range(n+1):
    if i <= (k - 1):
        A.append(1)
    else:
        A.append(sum(A[i-3:i]))
print(A[-1])
