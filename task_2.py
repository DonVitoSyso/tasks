# Программа, которая принимает строку, содержащую уравнение, написанное в
# обратной польской нотации (RPN), в качестве первого аргумента, вычисляет уравнение и
# выводит результат через alert и log.

def func_operator(op1, op2, op):
    x1, x2 = int(op1), int(op2)
    if op == '*':
        x1 *= x2
    elif op == '/':
        x1 /= x2
    elif op == '%':
        x1 %= x2
    elif op == '+':
        x1 += x2
    else:
        x1 -= x2

    return x1


operators = ['*', '/', '%', '+', '-']
stack = []

while True:
    equation = input("Введите уравнение:").split()

    for op in equation:
        # Проверка на корректность введенных данных
        if op in operators and len(stack) > 1:
            # проверка на ноль
            if int(stack[(len(stack))-1]) == 0 and op == '/':
                # print("Делить на ноль нельзя!")
                stack.clear()
                break
            # рассчитываем значение первого оператора и вносим в список
            else:
                stack.append(func_operator(stack.pop(len(stack) - 2), stack.pop(len(stack) - 1), op))
        elif op.isdigit():
            stack.append(op)
        # elif len(stack) < 2 and op in operators:
        #     # print(f"Оператор: '{op}' - стоит не верно (нет операндов для вычисления)")
        #     stack.clear()
        #     break
        else:
            # print("Некорректный символ: ", op)
            stack.clear()
            break

    # Вывод ответа, если в стэке остался один элемент
    if len(stack) == 1:
        print("Ответ:", stack[0])
        break
    else:
        print('KO')
    stack.clear()
