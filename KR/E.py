__author__ = 'student'

def f1(x):
    return(1+x*x)
def f2(x):
    return(-2-x*x)
x, y = list(map(float, input().split()))
if y > f1(x) or y < f2(x):
    print('YES')
else:
    print('NO')
