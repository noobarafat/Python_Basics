numbers = [2, 2, 4, 5, 5, 5, 5, 6, 8, 0, 2, 7, 8]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)