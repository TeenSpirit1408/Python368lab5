n = int(input())
A = list(map(int, input().split()))
if len(A) == n:
    max = max(A)
    min = min(A)
    k = 0
    l = max
    for i in range(n//2):
        for j in range(n):
            if (A[j] > k) and (A[j] < max):
                k = A[j]
            if (A[j] < l) and (A[j] > min):
                l = A[j]
        max = k
        min = l
        k = 0
        l = max
    print(min)
