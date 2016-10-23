import string
file_input1 = open('/home/user/Рабочий стол/img1.txt', 'r')
file_input2 = open('/home/user/Рабочий стол/input1.txt', 'r')
output = open('/home/user/Рабочий стол/output.txt', 'w')
words = file_input1.read()
text_for_translation = file_input2.read()

# Возвращает слоаврь
def dictionary(s):
    A = list(s.split('\t-\t'))  # Помещаем в массив элементы, разделйнные табами и тире
    B = []
    for i in range(len(A)):    # Помещаем в массив эелементы, разделённые и табами с тире, и переводами стргоки
        if '\n' in A[i]:
            B.extend(list(A[i].split('\n')))
        else:
            B.append(A[i])
    A = []    # Помещаем в массив только англ слова
    for i in range(0, len(B), 2):
        A.append(B[i])
    C = []    # Помещаем в массив только русс слова
    for i in range(1, len(B), 2):
        C.append(B[i])
    vocab = {a: c for a, c in zip(A, C)}    # Создаём словарь
    return vocab

vocab = dictionary(words)
text_for_translation = ''.join([elem if elem not in string.punctuation else ' ' for elem in text_for_translation])
# Убираем все запятые, точки и т.д.
text = list(text_for_translation.split())    # Всё помещаем в массив

text_true = []
# Переводим к нижнему регистру
for elem in text:
    elem = elem.lower()
    text_true.append(elem)

# Делаем перевод
translation = ''
for elem in text_true:
    if elem in vocab:
        translation += str(vocab[elem])
        translation += ' '
    else:
        translation += str(elem)
        translation += ' '

print(translation, file=output)
