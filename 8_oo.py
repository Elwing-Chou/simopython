# https://docs.python.org/3/reference/datamodel.html#object.__add__
class Person:
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    # method
    def calbmi(self):
        bmi = self.weight / (self.height / 100) ** 2
        return bmi

    def __str__(self):
        return "{}: {}".format(self.name, self.calbmi())

p1 = Person("Elwing", 175, 75)
bmi = p1.calbmi()
# print(p1) -> str(p1) -> p1.__str__()
print(p1)
print(bmi)

p2 = Person("Bob", 180, 75)
bmi = p2.calbmi()
print(bmi)