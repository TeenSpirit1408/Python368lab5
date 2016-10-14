__author__ = 'student'


k = 0
sum = 1
x = int(input())
a = 0
b = 1
c = 0
while sum < x:
    c = b
    b = a + b
    a = c
    sum += b
    k += 1
print(k+1)
