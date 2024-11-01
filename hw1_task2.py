a = input()
d = {')': '(',
     ']': '[',
     '}': '{'}
d1 = []
for i in a:
    if i in d.values():
        d1.append(i)
    elif i in d.keys():
        if d1 == [] or d[i] != d1.pop():
            print('False')
            break
print('True')