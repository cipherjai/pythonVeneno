tuple_1 = (1,2,3)
print(tuple_1)
print(len(tuple_1))
tups = ('one', 2, "Three")
print(tups[0])
print(tups[1])
print(tups[2])
print(tups[-2])
print(tups.index('Three'))
print(tups.index(2))
tups = ('one', 2, "Three", 2, "one", 4)
tups.count('one')

# tuple object does not support reassignmnent of item
# tups[0] = 'Two'
# print(tups)

def add(x, y):
    return x + y

# print add(3, 4)
# z = (5, 4)
# print add(*z) # this line will cause the values to be unpacked
# print add(z) # this line causes an error
