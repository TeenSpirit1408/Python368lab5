__author__ = 'student'


def f(x):
    a = 0
    while x != 0:
        a = a + x % 10
        x = x // 10
    return a
def pf(x):
    a = 0
    for i in range(1, x+1):
        if x % i == 0:
            a += 1
    if a == 2:
        return True
    else:
        return False

A, B, K = list(map(int, input().split()))
S = []
for i in range(A, B+1):
    if pf(i) == True and f(i) == K:
        S.append(i)
print(*S)