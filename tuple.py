tuple1 = (0, 1, 2,3, 4)
a = list(tuple1)
a[0] = 4
tuple1 = tuple(a)
print(tuple1)