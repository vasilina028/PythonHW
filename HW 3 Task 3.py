def capitalize(word):

    #f_char_code - код первого символа

    f_char_code = ord(word[0])

    if 97 <= f_char_code <= 122:
        capitalized_char_code = f_char_code - 32
        capitalized_f_char = chr(capitalized_char_code)
        part_word = word[1:]

        capitalized_word = capitalized_f_char + part_word

        return capitalized_word
    else:
        return word
#пример использования
print(capitalize("i love cats"))