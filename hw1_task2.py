def palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

input_line = input("Строка: ")
if palindrome(input_line):
    print("Палиндром")
else:
    print("Не палиндром")
