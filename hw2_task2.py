from collections import deque

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = deque(sorted(list1 + list2))
print(result)  # deque([1, 2, 3, 4, 5, 6, 7, 8])
