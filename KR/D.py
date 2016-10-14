__author__ = 'student'


A = list(map (int, input().split()))
k = 6
B = []
for i in range(3):
    B.append([])
    for j in range(3):
        B[i].append(A[k])
        k += 1
    k -= 6
for i in range(3):
    print(*B[i])
