f = open('/home/user/Рабочий стол/input.txt', 'r')
s = f.read()
max = 0
A = list(map(int, s.split()))
n = A.pop(0)
k = A.pop(-1)
for i in range(n):
    if sum(A[i:k+2]) > max:
        max = sum(A[i:k])
        k += 1
        print(max)
print(max)


