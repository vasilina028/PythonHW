sum = 0
for num in range(2, int(input()) + 1):
    check = True
    for Del in range(2, num):
        if num % Del == 0:
            check = False
            continue
    if check:
        sum += num
print(sum)
