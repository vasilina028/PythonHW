def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return (dx ** 2 + dy ** 2) ** 0.5
#пример использования
x1, y1, x2, y2 = 1.0, 2.0, 3.0, 4.0
dist = distance(x1, y1, x2, y2)
print(f"Расстояние между точками ({x1}, {y1}) и ({x2}, {y2}) равно {dist:.2f}")
