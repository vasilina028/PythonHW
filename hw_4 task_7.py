def even_numbers(numbers):
    e_nums = []
    for n in numbers:
        if n % 2 == 0:
            e_nums.append(n)
    return e_nums

numbers = list(range(1, 11))
e_nums = even_numbers(numbers)
print(e_nums)
