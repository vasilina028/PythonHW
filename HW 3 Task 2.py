def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    else:
        result = a
        for i in range(n - 1):
            result *= a
        return result
#пример использования
print(power(4, -2))