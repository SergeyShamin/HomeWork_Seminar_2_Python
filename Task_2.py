'''Напишите программу, которая принимает на вход число N и выдает
набор произведений чисел от 1 до N'''

number = int(input('Введите число N: '))
multiply = 1

for i in range(1, number + 1):
    multiply *= i 

    print(multiply)