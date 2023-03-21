# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь вводит натуральное 
# число N – количество элементов в массиве и число, которое 
# необходимо проверить - X. Заполните массив случайными натуральными 
# числами от 1 до N. Выведите, ближайший к X элемент. Если есть 
# несколько элементов, которые равноудалены от X, выведите 
# наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

length_array = int(input('Введите длину массива: '))
x = int(input('Введите целое положительное число, ближайшее (меньшее, если есть)'
              + ' к которому нужно найти в массиве: '))

array = [random.randint(1, length_array) for _ in range(length_array)]
print(array)
desired_number = 0 
for i in range(length_array):
    if(array[i] < x and array[i] > desired_number): 
        desired_number = array[i]
if(desired_number != 0):
    print(f'Ближайшее меньшее число к {x} равно {desired_number}')
else:
    desired_number = length_array
    for i in range(length_array):
        if(array[i] > x and array[i] < desired_number): 
            desired_number = array[i]
    print(f'Ближайшего меньшего числа к {x} нет.'
          + f' Ближайшее большее число к {x} равно {desired_number}.')