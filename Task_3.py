'''Задайте список из n чисел последовательности (1+1/n)**n и
выведите на экран их сумму'''

n = int(input('Введите n: '))

lst = []

for i in range(1, n):
    a = (1 + 1 / i) ** i
    lst.append(a)
    
sum = 0
for i in lst:
    sum += i
    
print(sum)