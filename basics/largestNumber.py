numbers = [2, 4, 5, 34, 55, 6, 56, 43, 78, 45, 5, 56, 343, 4, 3, 56]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
