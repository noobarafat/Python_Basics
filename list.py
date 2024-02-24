# myList = [1,2, 3,4, 5,6]
# # for i in range(0, 9):
# #     myList.append(i)
# print(myList)

# thisList = ['apple', 'banana', 'cherry', 'jackfruit']
# print(type (thisList))


# list1 = ['abc', 34, True, 49, 'male']
# for i in range(0, len(list1)):
#     print(type(list1[i]))


# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# print(thisList[2:4])

# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# print(thisList[:2])

# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# print(thisList[2:])


# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# thisList.remove('apple')
# print(thisList)


# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# thisList.pop(2)
# print(thisList)


# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# del thisList[0]
# print(thisList)

# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# thisList.clear()
# print(thisList)

# thisList = ['apple', 'komola', 'angor', 'kocu', 'loti']
# [print(x) for x in thisList]


# fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']

# newList = []
# for x in fruits:
#     if 'a' in x:
#         newList.append(x)
# print(newList)


# fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']
# newList = [x for x in fruits if 'a' in x]
# print(newList)


# fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']
# newList = [x for x in fruits if x!='apple']
# print(newList)

# newList = [x for x in range(10) if x<5]
# print(newList)


# fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']
# newList = [x for x in fruits ]
# print(newList)


# fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']
# newList = [x.upper() for x in fruits ]
# print(newList)

# fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']
# newList = ['hello' for x in fruits ]
# print(newList)

fruits = ['apple', 'komola', 'angor', 'kocu', 'loti']
newList = [ x if x!= 'apple' else "orange" for x in fruits ]
print(newList)