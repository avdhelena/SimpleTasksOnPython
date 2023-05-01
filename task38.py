#todo Задача 1. Транспонирование матрицы, transpose(matrix)
# Создайте списковое включение, которое генерирует следующую последовательность: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10
N = 10
lst = [index for index in range(1, N+1)
             for i in range(index)]
print("Task 01:")
print(lst)

#todo Задача 2. Транспонирование матрицы, transpose(matrix)
# Написать функцию transpose(matrix), которая выполняет транспонирование матрицы. Решить с использованием списковых включений.
# Пример:
# >>> transpose([[1, 2, 3], [4, 5, 6]])
#
# [[1, 4], [2, 5], [3, 6]]
#
#
# ||1 2 3||      ||1 4||
# ||4 5 6||  =>  ||2 5||
#                ||3 6||
#
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
trans_matrix = [[row[index] for row in matrix] for index in range(len(matrix[0]))]
print("Task 02:")
print(f"matrix: {matrix}")
print(f"trans_matrix: {trans_matrix}")




# #todo Задача 3. Найти сумму элементов матрицы
# Написать msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)


matrix_sum = sum([element for row in matrix for element in row])
print(f"matrix_sum: {matrix_sum}")
msum = 0
for element in [element for row in matrix for element in row]:
    msum += element
print(f"msum: {msum}")





matrix_02 = [[5, 2, 16], [8, 5, 9], [3, 2, 9], [1, 11, 4]]
matrix_sum = [[matrix[i][j]+matrix_02[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

print(f"matrix_01: {matrix}")
print(f"matrix_02: {matrix_02}")
print(matrix_sum)

#print(len(matrix))
#print(len(matrix[0]))
