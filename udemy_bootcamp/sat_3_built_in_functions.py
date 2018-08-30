from functools import reduce

# 1 print(list(map(lambda word: len(word), input("> ").split(' '))))
# print(list(map(len, input().split())))
#
# 2 print(list(reduce(list.__add__, input("For number > ").split(" "))))
# print(reduce(lambda x,y: x*10 + y, list(map(int, input().split(", ")))))

# 3 print(list(filter(lambda w: True if w[0] != "h" else False, input(">").split(" "))))
# print(list(filter(lambda word: word[0] == 'h', input(">").split(" "))))

#4

# l1 = input("1>").split(" ")
# l2 = input("2>").split(" ")
#
# sent = [word1 + connector + word2 for (word1, word2) in zip(l1, l2)]

# list comprehension
l = ['a', 'b', 'c']
print({key:value  for value,key in enumerate(l)})


# print(map(int, input().split(" ")))
#
# # count matches the index
# print(len(num for count,num in enumerate(l) if num == count))
