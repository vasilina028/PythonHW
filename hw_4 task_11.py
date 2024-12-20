def sqrt_gen():
    num = 0
    while True:
        value = (yield num ** 0.5)
        if value is not None:
            num = value
        else:
            num += 1

# Пример использования
gen = sqrt_gen()
next(gen)

for _ in range(10):
    print(next(gen))
    gen.send(None)