def fib(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        result = [1, 1]
        for i in range(2, n):
            result.append(result[-1] + result[-2])
        return result

#пример использования
print(fib(5))
print(fib(10))