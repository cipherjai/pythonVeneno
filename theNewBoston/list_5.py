# lists

players = [29, 58, 66, 71, 87]
# always starts counting with 0

print(players[2])

# changing value inside

players[2] = 68
print(players)

# adding list to a list
print(players + [90, 91, 100])

# but the original list doesn't undergoes any change
print(players)

# when wee want to change the list permanently
# use of append
players.append(56)

# how to slice up the items with our lists
print(players[:2])
# doesn't includes last index

# set new values at once
players[:2] = {0, 0}
print(players)
# setting the values to empty , ot zero , i.e delete the itwms

# even the deleting of values is possible
players[:1] = []
print(players)

players[3:4] = []
print(players)
# removing all from list , just set the items to empty
players[:] = []

print(players, "is empty")
