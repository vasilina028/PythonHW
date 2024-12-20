def matrix_m(matrix1, matrix2):

    r1 = len(matrix1)
    c1 = len(matrix1[0])
    c2 = len(matrix2[0])

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Пример использования
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

result = matrix_m(matrix1, matrix2)
print(result)