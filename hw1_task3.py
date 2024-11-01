stack = ["3", "5", "+"]
array = []
for element_num in range(len(stack)):
    if stack[element_num] == '/':
        array.append(int(array[len(array) - 2]) // int(array[len(array) - 1]))
        array.pop(len(array) - 2)
        array.pop(len(array) - 2)
        continue
    elif stack[element_num] == '*':
        array.append(int(array[len(array) - 2]) * int(array[len(array) - 1]))
        array.pop(len(array) - 2)
        array.pop(len(array) - 2)
        continue
    elif stack[element_num] == '+':
        array.append(int(array[len(array) - 2]) + int(array[len(array) - 1]))
        array.pop(len(array) - 2)
        array.pop(len(array) - 2)
        continue
    elif stack[element_num] == '-':
        array.append(int(array[len(array) - 2]) - int(array[len(array) - 1]))
        array.pop(len(array) - 2)
        array.pop(len(array) - 2)
        continue
    else:
        array.append(stack[element_num])
print(array[0])