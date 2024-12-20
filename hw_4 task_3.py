def count_strings(length):
    total = 2 ** length
    with_ab = 2 * (2 ** (length - 2))
    return total - with_ab

print(count_strings(6))