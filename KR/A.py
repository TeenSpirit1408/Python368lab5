__author__ = 'student'


v = int(input())
t = int(input())
s = 0
if v*t > 0:
    s = (v*t) % 109
else:
    s = (109 + ((v*t)%109)) % 109
print(s)
