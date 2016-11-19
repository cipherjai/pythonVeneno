#formattted String
# "" around something is a format string
#Embedding variables inside a String

#format sequence

myName = 'Jai Gupta'
myAge = 22 # not a lie
myHeight = 74 # inches
myWeight = 160 #lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'

print ("Let's talk about %s !" % myName)
print ("He's %d inches tall !" % myHeight)
print ("He's %d pounds Heavy!" % myWeight)
print ("If I add %d, %d, and %d, I get %d." %(myAge, myHeight, myWeight, myWeight+myAge+myHeight))

print ("He's %d inches tall !" % (myHeight*2.54))

print (" How to print this %d even after using it")

