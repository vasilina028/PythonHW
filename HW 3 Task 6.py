def reverse(n):
    if n == 0:
        return
    else:
        print(n % 10, end="")
        reverse(n // 10)
#пример использования
reverse(543210)