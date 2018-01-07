# Formatted String
# "" around a something means to be formatted string
# Embedding variables inside a string

myName = 'Jai Gupta'
myAge = 22  # not a lie
myHeight = 74  # inches
myWeight = 160  # lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'
isSingle = True

# formatter
firstName = "Jai"
lastName = "Gupta"
print("Dummy Run")
print("Naam to pata hi hoga", firstName, lastName)
print("Bhai ka naam hai %s %s aur bhai %rly single hai." % (firstName, lastName, isSingle))
print("%d hai mera weight, aur height %d, %s eyes hain meri." % (myWeight, myHeight, myEyes))

# %s > string
# %d > integer
# %f > float
print("He is %d inches tall" % (myHeight * 2.54))
print("He is %f inches tall" % (myHeight * 2.54))
print()

# printing without the formatter
print('I am %s inches tall' % myHeight)
myHeight *= 5
# augmented for myHeight =  myHeight * 5
print('Hamari height hai %s' % myHeight)

# concatenating string
print(firstName + lastName)
print(firstName, lastName)

# using the precision formatter
myHeight /= 5
print("He is %.2f inches tall" % (myHeight * 2.54))

# quantize
from decimal import Decimal, ROUND_DOWN

heightCalculated = Decimal(str(myAge * 2.75)).quantize(Decimal('.03'))
print(heightCalculated, "is his height.")
