def getRow(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
    return row

print(getRow(3))
print(getRow(0))
print(getRow(1))