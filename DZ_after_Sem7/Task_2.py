# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по 
# номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк 
# и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно 2 аргумента, как, 
# например, у операции умножения.

import os
os.system('cls')

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(f'{operation(i, j)}', end=" ")
        print()

rows=int(input('Введите количество строк: '))
columns=int(input('Введите количество столбцов: '))
print_operation_table((lambda rows, columns: rows * columns), rows, columns)