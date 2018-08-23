# Objects

class BankAccount:
    """ Class for Bank Accounts"""

    type = 'Normal Account'    # variable shared by all objects of the class

    def __init__(self, name):  # This method is used to initialize an object on its creation
        # default variables unique to each object:
        self.userName = name
        self.balance = 0.0

    # Object Methods:

    def showBalance(self):
        print (self.balance)
        return

    def withdrawMoney(self, amount):
        self.balance -= amount
        return

    def depositMoney(self, amount):
        self.balance += amount
        return

class Sample(object):
    """docstring for Sample."""
    def __init__(self, arg):
        super(Sample, self).__init__()
        self.arg = arg

class Dog(object):
    """docstring for Dog."""
    species = "Mammal"
    # special method
    def __init__(self, breed, name, fur = True):
        self.name = name
        self.fur = fur
        self.breed = breed

sam = Dog(breed = "Lab", name = "Genii", fur = False)
print(sam)
print(sam.breed)
print(sam.name)
print(sam.fur)
print(sam.species)
