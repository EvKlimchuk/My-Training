# Функции в Python. Функции с параметром
# Домашняя работа. Задача "Матрица во плоти"

def get_matrix(n, m, value):
    matrix = [ ]
    for i in range(n):
        row = [ ]
        matrix.append(row)
        for j in range(m):
            row.append(value)
    return matrix

result_1 = get_matrix(2, 2, 10)
print("Result 1: ", result_1)

result_2 = get_matrix(3, 5, 42)
print("Result 2: ", result_2)

result_3 = get_matrix(4, 2, 13)
print("Result 3: ", result_3)



