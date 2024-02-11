class Person:
    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, years):
        self.age += years


person1 = Person("Mike", 34, 233)
person2 = Person("sara", 34, 233)

del person2
print(Person.amount)
