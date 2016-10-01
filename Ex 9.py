f = open('/home/user/Рабочий стол/input.txt', 'r')
s = f.read()
print(s)
line = list(map(int, f.readline().split()))
print(line)


