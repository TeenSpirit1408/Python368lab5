__author__ = 'student'

x = int(input())
Max1 = 1
Max2 = 1
while x != 0:
    if x >= Max2 and x <= Max1:
        Max2 = x
    if x > Max1:
        Max2 = Max1
        Max1 = x
    x = int(input())
print(Max2)
