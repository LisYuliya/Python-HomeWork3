'''Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

lenght = int(input('Введите длину списка: '))
some_list = []

for i in range(0, lenght):

    n = float(input('Введите число: '))
    some_list.append(round(n - int(n), 3))

min_value = some_list[0]
max_value = some_list[0]

for j in some_list:
    if j > 0:
        if j > max_value:
            max_value = j
        elif j < min_value:
            min_value = j

print('Разница между максимальным и минимальным значением дробной части элементов = ', max_value-min_value)

