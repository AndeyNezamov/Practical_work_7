def calculator_upgrade(num):
    action = int(input('Введите номер действия: \n'
                       '1 - сумма цифр\n'
                       '2 - максимальная цифра\n'
                       '3 - минимальная цифра\n'))
    if action == 1:
        summa = 0
        for i in str(num):
            summa += int(i)
        return f'сумма цифр: {summa}'

    elif action == 2:
        max_number = 0
        for i in str(num):
            if int(i) > int(max_number):
                max_number = int(i)
        return f'максимальная цифра: {max_number}'

    elif action == 3:
        min_number = num // 10 ** (len(str(num)) - 1)
        for i in str(num):
            if int(i) < int(min_number):
                min_number = int(i)
        return f'минимальная цифра: {min_number}'

print(calculator_upgrade(int(input('Введите число: '))))