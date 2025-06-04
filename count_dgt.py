number = input("Введите число: ")
digit_counts = {}

for digit in number:
    if digit.isdigit():
        digit_counts[digit] = digit_counts.get(digit, 0) + 1

print("Количество цифр в числе:")
for digit, count in sorted(digit_counts.items()):
    print(f"{digit}: {count}")