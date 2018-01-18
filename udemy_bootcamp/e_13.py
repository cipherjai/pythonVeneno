# Numbers in Python
# 3 types of numbers are present in python
"""
 1. Integers 2 , -2
 2. Floating point, decimal -> 2.0, -2.5
 3. Exponent E -> 4E2 . Means 4 times 10 to the power of 2
"""

print(3 / 2)
print(3. / 2)

# call float to type cast
print(float(34) / 2)

# Also check python notebook in conjunction with the same
# there using from__future__import division

print(2 ** 3)
print(4 ** 5)
print(4 ** 0.5)
# follows an order
print(2 + 10 * 10 + 3)
print("Difference between classic division and true division")

# Classic vs True
print((2 * 3) * (6 * 7))

# if printed like this ((2*3)(6-7))
# is not a callable object

print(" Dil me mere hai dar de disco ''''''' ")

a_very_long_string = "Simply new very long string is here!"
print(a_very_long_string[:16])

print(len(a_very_long_string))

import datetime
d = datetime.date.today()
print(d)
print(str(d))
print(repr(d))

x = "There are %d types of people"
print("I said: %r." % x)
y = "ZThose who know %s and those who %s." % ("binary", "don't")
print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
