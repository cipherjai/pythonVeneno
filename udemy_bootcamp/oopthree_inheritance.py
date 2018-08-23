class Animal(object):
    """docstring for Animal."""
    def __init__(self):
        super(Animal, self).__init__()
        print("Animal created !")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    """docstring for Dog."""
    def __init__(self):
        Animal.__init__(self)
        print("Dog created !")

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print("Woof!")


d = Dog()
d.whoAmI()
d.bark()
