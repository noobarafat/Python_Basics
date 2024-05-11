class Shopping_Cart:
    def __init__(self):
        self.lst = []

    def add(self, item, qnty):
        self.lst.append((item, qnty))

    def remove(self, item):
        for items in self.lst:
            if items[0] == item:
                self.lst.remove(items)
                break

    def display(self):
        for items in self.lst:
            print(f"{items[0]} - {items[1]}")


obj = Shopping_Cart()
obj.add("Guava", 20)
obj.add("Mango", 10)
obj.add("Orange", 30)
print(f"Current items in cart: ")
obj.display()
print()
obj.remove("Orange")
print(f"Current items in cart after removing Orange: ")
obj.display()
print(type(obj.lst))