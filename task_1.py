# Программа, которая принимает неопределенное количество строк в аргументах.
# Для каждого аргумента программа выводит на стандартном выводе "ОК",
# если выражение правильно заключено в скобки, в противном случае она выводит "KO".

# Варианты для проверки алгоритма
t1 = '(johndoe)'
t2 = '([)]'
t3 = ['', '{[(0 + 0)(1 + 1)](3*(-1)){()}}']
t4 = ['', '{[(0 + 0)(1 + 1)](3*(-1)){()}}', '([)]']

# Список всех скобок для сравнения
staples = ['(', '[', '{', ')', ']', '}']
# Пустой список всех скобок
stpls = []

d = input("Введите примеры для проверки:").split()
print(d)

# Проходимся по аргументам строки
for i in d:
    # Проверяем не является ли сам аргумент строкой
    if len(i) > 0:
        for j in i:
            # Открывающаяся скобка, тогда в список
            if j in staples[0:3]:
                stpls.append(j)
            elif j in staples[3:6]:
                # Проверка закр.скобки - вернаяый или нет порядок
                if j == staples[staples.index(stpls[-1]) + 3]:
                    del stpls[-1]
                else:
                    print("KO")
                    break
    else:
        if i in staples[0:3]:
            stpls.append(i)
        elif i in staples[3:6]:
            stpls.append(i)

if len(stpls) == 0:
    print("OK")
