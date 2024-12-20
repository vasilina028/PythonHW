num = list(range(1, 11))
sqrt = list(map(lambda x: x**2, num))
for num, sqrt in zip(num, sqrt):
    print(f"{num}\t{sqrt}")