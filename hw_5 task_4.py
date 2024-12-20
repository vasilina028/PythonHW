data = [10, 15, 8, 12, 20]

df = {'Числовые данные': data}

c_sum = 0
sums = []
for x in data:
    c_sum += x
    sums.append(c_sum)

df['Накопительная сумма'] = sums

for i, row in enumerate(zip(df['Числовые данные'], df['Накопительная сумма'])):
    print(f"{i}. Числовые данные: {row[0]}, Накопительная сумма: {row[1]}")