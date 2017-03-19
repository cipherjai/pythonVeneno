def add(a, b):
    print("Adding %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("Subtracting %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("Multiplying %d X %d" % (a, b))
    return a * b


def divide(a, b):
    print("Dividing %d / %d" % (a, b))
    return a / b


print("Let's do some juggling with maths!")


age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print("Age: %d, height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# Puzzle


print("Here is a puzzle !")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, ", Can you do it by Hand?")

