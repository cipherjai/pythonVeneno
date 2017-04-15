# Classes Modules Objects

# constructs in python called as Class

# Modules
import ex40assist_2
my_stuff = {'apple': "I am apples!"}
print(my_stuff['apple'])

# in modules, we get X from Y


def apple():
    print("I am Apples!")

tangerine = "Living reflection of a dream"

# classes
import ex40


class MyStuff(object):

    def __init__(self):
        self.tangerine = None
        ex40.tangerine = "And now a thousand years between!"

    def apple(self):
        print("I am classy apples!")

things = MyStuff()
things.apple()
print(things.tangerine)
