A = list(map(int, input().split()))
if len(A) == 10:
    k = 0
    i = 1
    for i in range(1, len(A)):
        if (A[i] != 2) and (A[i-1] == 2):
            A[i-1] = 0
            k += 1
    a = sum(A)
    b = len(A) - k
    x = a // b
    print(x)
