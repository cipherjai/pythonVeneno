# Use reduce to combine numbers
from functools import reduce
# we define a list of integers
numbers = [1, 4, 6, 2, 9, 10]
# Define a new function combine
# Convert x and y to strings and create a tuple from x,y
def combine(x,y):
  return "(" + str(x) + ", " + str(y) + ")"

print(numbers)
print(type(reduce(combine,numbers)))
print(reduce(combine,numbers))


# we define a list of integers
numbers = [1, 4, 6, 2, 9, 10]


print(numbers)
print(reduce(lambda x,y: "(" + str(x) + ", " + str(y) + ")",numbers))

list_of_randon_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12, 13], [5]]
print(list(reduce(list.__add__, list_of_randon_numbers)))
print(list(set(reduce(list.__add__, list_of_randon_numbers))))
