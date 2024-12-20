def unique(str):
    result = []
    for char in str:
        if char not in result:
            result.append(char)
    return result

# Пример использования
string = "Hello, World!"
uni_char = unique(string)
print(uni_char)