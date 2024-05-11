class Shopping_Cart:

    def __init__(self):
        self.dict={}
    def add(self,item,qnty):
        self.dict[item]=qnty
    def remove(self,name):
        for item in self.dict:
            if name==item:
                del self.dict[item]
                break
    def display(self):
        for item in self.dict:
            print(f"{item} - {self.dict[item]}")

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