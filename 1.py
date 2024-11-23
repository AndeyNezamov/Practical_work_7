# Напишите функцию summa_n, которая принимает одно целое положительное число N и
# выводит сумму всех чисел от 1 до N включительно.

def summa_n(num):
    summa = 0
    for i in range(num+1):
        summa += i
    return summa

print(summa_n(int(input('Введите число: '))))