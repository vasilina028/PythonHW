def skobki(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

test = [
    "(({[]}))",  # True
    "{(})",      # False
    '([])[[]]',  # True
    ")())[[]]",   # False
    "(())[[]]",   # True
    '([])'       
]

for case in test:
    print(f"{case}: {skobki(case)}")
