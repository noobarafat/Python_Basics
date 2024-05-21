# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # matrix[0][1] = 20
# # print(matrix[0][1])
#
# for row in matrix:
#     for item in row:
#         print(item)
#

numbers = [5, 2, 1, 7, 4]
# numbers.append(9)
# numbers.insert(0, 23)
# numbers.remove(5)
# # numbers.clear()
# numbers.pop()
print(2 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
