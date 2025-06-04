def create_abbreviation(phrase):
    words = phrase.split()
    abbreviation = []
    for word in words:
        if word:  # проверяем, что слово не пустое
            first_char = word[0]
            if first_char.isalpha():  # проверяем, что первый символ - буква
                abbreviation.append(first_char.upper())
    return ''.join(abbreviation)

# Примеры использования
print(create_abbreviation("Today I learned"))  # TIL
print(create_abbreviation("Высшее учебное заведение"))  # ВУЗ
print(create_abbreviation("Кот обладает талантом"))  # КОТ
print(create_abbreviation("Ар 2 Ди #2"))  # АД
print(create_abbreviation("Анна-Мария Волхонская"))  # АВ