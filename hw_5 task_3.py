matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

total_sum = sum(sum(row) for row in transposed)

print("Исходная:")
for row in matrix:
    print(row)

print("\nТранспонированная:")
for row in transposed:
    print(row)

print(f"\nСумма транспонированной матрицы: {total_sum}")