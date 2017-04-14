# List Manipulations

my_stuff = []

my_stuff.append('hello')

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Manipulating stuff. Buenas Noches")

print(stuff[1])  # at position 1
print(stuff[-1])  # at position last
print(stuff.pop())  # popping the last one and delivering out
print(' '.join(stuff))  # joining with regex function with a parameter ' '
print('#'.join(stuff[3:5]))  # ranging with position 3 and ending at y-1 with parameter regex '#'

# experimenting

