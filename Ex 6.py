n = int(input())
A = list(map(int, input().split()))
if len(A) == n:
    max = max(A) + 1
    min = min(A) - 1
    k = 0
    l = max
    for i in range(n//2):
        for j in range(n):
            if (A[i] > k) and (A[i] < max):
                k = A[i]
            if (A[i] < l) and (A[i] > min):
                l = A[i]
        max = k
        min = l
    print(max, min)
