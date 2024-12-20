from collections import deque

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return len(key) % self.size

    def insert(self, key):
        index = self.hash(key)
        for item in self.table[index]:
            if item == key:
                return
        self.table[index].append(deque([key]))

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: ", end="")
            for item in chain:
                print(list(item), end=" -> ")
            print("None")