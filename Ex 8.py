n = int(input())
A = []
B = []
count = 0
for i in range(n):
    k, n = map(int, input().split())
    A.append(k)
    B.append(n)
t = int(input())
for i in range(len(A)):
    if (t >= A[i]) and (t <= B[i]):
        count += 1
print(count)
