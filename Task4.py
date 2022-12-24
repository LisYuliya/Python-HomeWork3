'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

### Вариант решения №1 ###

num = int(input('Введите число: '))
num2 = bin(num)[2:]
print(num2)


### Вариант решения №2 ###

num = int(input('Введите число: '))
num2 = ""

while num != 0:
    num2 = str(num % 2) + num2
    num //= 2
print(num2)