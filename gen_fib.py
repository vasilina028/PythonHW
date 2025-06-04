def fibonacci(n):
    n1, n2 = 0, 1
    for _ in range(n):
        yield n1
        n1, n2 = n2, n1 + n2

# Пример использования:
for num in fibonacci(6):
    print(num)