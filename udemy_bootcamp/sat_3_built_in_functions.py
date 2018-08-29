from functools import reduce

# print(list(map(lambda word: len(word), input("> ").split(' '))))
#
# print(list(reduce(list.__add__, input("For number > ").split(" "))))

print(list(filter(lambda w: True if w[0] != "h" else False, input(">").split(" "))))
