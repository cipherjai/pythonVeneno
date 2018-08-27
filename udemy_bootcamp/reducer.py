# Use reduce to combine numbers
from functools import reduce


# we define a list of integers
numbers = [1, 4, 6, 2, 9, 10]
# Define a new function combine
# Convert x and y to strings and create a tuple from x,y
def combine(x,y):
  return "(" + str(x) + ", " + str(y) + ")"

# Use reduce to apply combine to numbers
from functools import reduce

print(numbers)
print(type(reduce(combine,numbers)))
print(reduce(combine,numbers))


# we define a list of integers
numbers = [1, 4, 6, 2, 9, 10]


print(numbers)
print(reduce(lambda x,y: "(" + str(x) + ", " + str(y) + ")",numbers))
