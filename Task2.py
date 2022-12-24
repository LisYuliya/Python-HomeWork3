'''Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

lenght = int(input('Введите длину списка: '))
some_list = []
new_list = []
multiplication = 0
for i in range(0, lenght):

    n = int(input('Введите число: '))
    some_list.append(n)

if lenght % 2 != 0:
    for j in range(0, int((lenght/2)+1)):

        multiplication = some_list[j]*some_list[lenght-1]
        new_list.append(multiplication)
        j += 1
        lenght -= 1
else:
    for j in range(0, int(lenght/2)):

        multiplication = some_list[j]*some_list[lenght-1]
        new_list.append(multiplication)
        j += 1
        lenght -= 1

print(some_list, ' -> ', new_list)
