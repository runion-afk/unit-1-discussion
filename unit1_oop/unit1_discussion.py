"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy

class Item:
    total = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Item.total += 1
    def show(self):
        return f"{self.name}: ${self.price}"

class Phone(Item):
    category = "Tech"
    def __init__(self, name, price, brand, apps):
        super().__init__(name, price)
        self.brand = brand
        self.apps = apps
    def ring(self):
        return "Ring!"
    def show(self):
        return f"{self.brand} {self.name} with {len(self.apps)} apps"

def demonstrate_namespaces():
    p1 = Phone("A", 500, "BrandX", [])
    p2 = Phone("B", 600, "BrandY", [])
    print(Phone.category, p1.category)
    p1.color = "Red"
    print(p1.__dict__, p2.__dict__, Phone.__dict__)

def demonstrate_copying():
    p = Phone("C", 700, "BrandZ", ["Maps"])
    s_copy = copy(p)
    d_copy = deepcopy(p)
    p.apps.append("Game")
    # Shallow copy shares the app list. Deep copy makes a new list.
    print(p.apps, s_copy.apps, d_copy.apps)

def main():
    i = Item("Box", 10)
    print(i.show())
    p = Phone("Pro", 900, "BrandW", ["Mail"])
    print(p.show(), p.ring())
    demonstrate_namespaces()
    demonstrate_copying()

if __name__ == "__main__":
    main()