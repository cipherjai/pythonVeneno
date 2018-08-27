# creating anonymous functions

# not a block of statements
# just a def statements

# normal function
def square(num):
    result = num ** 2
    return result

print(square(5))

def cube(num):
    return num ** 3

def square(num): return num ** 2

lamb = lambda num: num ** 2

print(type (lambda num: num ** 2))
print(type (lamb))
print(lamb(100))

lamb_even = lambda num : num % 2 == 0
print(lamb_even(7))

# lamb_first = lambda s : if s.length >= 0: print (s[0])  else: print("Nothing is in there!")
# print(lamb_first("Something"))

# The syntax you're looking for:
#
# lambda x: True if x % 2 == 0 else False
# But you can't use print or raise in a lambda.

lamb_first =  lambda s : s[0] if len(s) != 0 else "Nothing is in there"
print(lamb_first("Something"))
print(lamb_first(""))

rev = lambda s: s[ : :-1]
print(rev("string"))

# taking multiple arguements

adder = lambda x,y : x+y
print(adder (2,3))

#   Map()
#   filter()
#   reduce()

# starting with Map ()
