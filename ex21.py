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


# ==============================
name = 23 + 43.0
print("%d , She's crazy !" % name)
# ==============================

# ======= Anu Doubt ======
print("============================")
first_number = 10.25
second_number = 7.5
print(first_number - second_number)

# error or something that is don't know
x = 20.55
y = 20.91
z = 20.50

print((x + y))
print(x - z)

# by jai
floating_point_values = 0.5
print ("%0.1f" % (floating_point_values))
print ("%0.11f" % (floating_point_values))
print ("%0.01f" % (floating_point_values))
print ("%0.011f" % (floating_point_values))

print("%0.1f" %(x - z))
print("%0.11f" %(x - z))
print("%0.01f" %(x - z))
print(float(x - z))
print()
# Python stores floats with 'bits', and some floats you just can't represent accurately, no matter how many bits of
# precision you have. This is the problem you have here. It's sorta like trying to write 1/3 in decimal with a limited
#  amount of decimals places perfectly accurate.

floating_point_values = 0.05
print ("%0.1f" % (floating_point_values))
print ("%0.11f" % (floating_point_values))
print ("%0.01f" % (floating_point_values))
print ("%0.011f" % (floating_point_values))
print ("%0.00f" % (floating_point_values))
print ("%0.001f" % (floating_point_values))
print ("%0.010f" % (floating_point_values))


# here's after all experiments
print ("%0.2f" % (x - z))
print ("%0.3f" % (x - z))

print("============================")

# Puzzle


print("Here is a puzzle !")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, ", Can you do it by Hand?")

