# Decision Making Wisely

print("Yoy enter the dark room with two  doors. Do you go through door no 1 or no 2? ")

door = input("> ")

if door == "1":
    print("There's a giant bear eating a cheese cake What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print("Well, doing %s is probably better.  Bear runs away." % bear)


elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    # x in range(1, 10)
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.  Good job!")
    elif insanity in range(3, 7):
        print("The insanity rots your eyes into a pool of muck.  Good job!")
    else:
        print("You're clever !")
        if 10 < (int(insanity)) < 12:
            print("Holy!")
else:
    print("You stumble around and fall on a knife and die.  Good job!")
