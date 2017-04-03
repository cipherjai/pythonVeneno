# lists and for loops

hairs = ['brown', 'blonde', 'red', 'black']
eyes = ['black', 'brown', 'green', 'blue']
theCount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in theCount:
    print("This is the count %d" % number)

for fruit in fruits:
    print("A fruit of type %s " % fruit)

for i in change:
    print("I got %r" % i)

# we can also build lists

elements = []

for i in range(0, 6):
    print("Adding %d to the list" % i)
    elements.append(i)


# now we print

for i in elements:
    print("Element was: %d" % i)

for eye in eyes:
    print("I love %s eyes." % eye)

for hair in hairs:
    print("I love girls with %s hairs!" % hair)


