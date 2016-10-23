file_input = open('/home/user/Рабочий стол/input2.txt', 'r')
file = file_input.read()

# Возвращает словарь
def dictionary(s):
    A = list(s.split(' : '))  # Помещаем в массив элементы, разделйнные двоеточиями.
    B = []
    for i in range(len(A)):    # Помещаем в массив эелементы, разделённые двоеточиями и переводами стргоки.
        if '\n' in A[i]:
            B.extend(list(A[i].split('\n')))
        else:
            B.append(A[i])

    # На данный момент имеем массив В, где соседние строки содержат страну и языки, на которых говорят в этой стране.

    countries = []  # Помещаем в массив только страны.
    for i in range(0, len(B), 2):
        countries.append(B[i])
    languages = []  # Помещаем в массив только языки.
    for i in range(1, len(B), 2):
        languages.append(B[i])

    # На данный момент имеем два массива, содержащие страны и языки, на которых говорят в этих странах отдельно

    countries_true = []    # Сюда поместим страны в кол-ве языков
    languages_true = []    # Сюда поместим языки в полном кол-ве

    # Этим циклом создаём два массива, в котором будут содержаться страны (кол-во одной страны может быть > 1), и языки
    # (отдельно друг от друга)

    for i in range(len(languages)):
        k = len(languages_true)
        languages_true.extend(languages[i].split())
        a = len(languages_true) - k
        for j in range(a):
            countries_true.append(countries[i])


    languages_real_true = []    # Запишем в этот массив все языки по одному разу
    countries_real_true = []    # Запишем в этот массив все страны, в которых говорят на данном языке
    k = 0

    # Этот цикл выполняет написанное выше

    for i in range(len(languages_true)):
        if languages_true not in languages_real_true:
            languages_real_true.append(languages_true[i])
            countries_real_true.append(countries_true[i])
            countries_real_true[k] += str(' ')
            for j in range(len(languages_true)):
                if languages_true[i] == languages_true[j] and i != j:
                    countries_real_true[k] += str(countries_true[j])
                    countries_real_true[k] += str(' ')
            k += 1

    # Создаём перевёрнутый словарь
    Countries_of_language = {language: country for language, country in zip(languages_real_true, countries_real_true)}
    # Создаём словарь
    return Countries_of_language

Countries_of_language = dictionary(file)
language = input()
if language in Countries_of_language:
    print(Countries_of_language[language])
