import string
file_input = open('/usr/share/licenses/python/LICENSE', 'r')

text_file = file_input.read()
text_file = ''.join([elem if elem not in string.punctuation else ' ' for elem in text_file])

massive = list(text_file.split())
massive_true = []
for elem in massive:
    elem = elem.lower()
    massive_true.append(elem)

A = dict()
for word in massive_true:
    if word not in A:
        A[word] = 1
    else:
        A[word] += 1

A = {A[word]: word for word in A}

for i in range(10):
    print(A[max(A)])
    del A[max(A)]
