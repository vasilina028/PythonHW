class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = [[nested_list, 0]]  # Стек хранит пары [список, текущий индекс]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            current_list, index = self.stack[-1]

            if index >= len(current_list):
                self.stack.pop()
                continue

            self.stack[-1][1] += 1  # Увеличиваем индекс для текущего списка

            element = current_list[index]
            if isinstance(element, list):
                # Если элемент - список, добавляем его в стек с индексом 0
                self.stack.append([element, 0])
            else:
                # Если элемент не список, возвращаем его
                return element

        raise StopIteration