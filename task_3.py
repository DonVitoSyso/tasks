# Программа, принимающая массив цифр, которая находит самый длинный
# подмассив с равным количеством четных и нечетных цифр


def func_ev_unev(number):
    if number%2:
        return False
    else:
        return True


def func_counter(massiv):
    even = 0
    uneven = 0
    for num in massiv:
        if func_ev_unev(int(num)):
            even += 1
        else:
            uneven += 1

    # вычисляем самую длинную последовательность, которую можно найти
    if even > uneven:
        return uneven
    elif even < uneven:
        return even
    else:
        return None


massiv = input("Введите массив цифр:")
mass_tmp = []
long = func_counter(massiv)

# Перебираем возможные варианты последовательностей
while True:
    for i in range(len(massiv)-long*2+1):
        mass_tmp.clear()
        mass_tmp.extend(massiv[i:i+long*2])
        if func_counter(mass_tmp) is None:
            break

    if func_counter(mass_tmp) is None:
        break
    # длинную последовательность уменьшаю и перепроверяю
    long = long//2

print(f'Саммый длинный подмассив: {"".join(mass_tmp)}')
