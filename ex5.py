# formattted String
# "" around something is a format string
# Embedding variables inside a String

#format sequence

myName = 'Jai Gupta'
myAge = 22 # not a lie
myHeight = 74 # inches
myWeight = 160 #lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'
# formatter

first_name = "Jai"
last_name = "Gupta"
print("Dummy Run")
print("The name is", first_name, last_name)
print("Bhai ka naam hai : %s %s aur bhai ki age hai : %d" %(first_name, last_name, myAge))
new_name = 'anu'
print('Mere ko %d print karna hai %d times')




# %s > string
# %d > integer
# %f > float
print ("Let's talk about %s !" % myName)
print ("He's %d inches tall !" % myHeight)
print ("He's %d pounds Heavy!" % myWeight)

# Multiple formats
# TODO: To check how to print %d
print("If I add %d, %d, and %d, I get %d." %(myAge, myHeight, myWeight, myWeight+myAge+myHeight))

print("He's %d inches tall !" % (myHeight*2.54))

print(" How to print this %d even after using it")

print("")

print ('Dummy Inside')
print (myTeeth + myHair)
# anyVariable = "LOL"*10.54 # unexpected indent
lol = "LOL"*10
print (lol)

# # More Strings ***

# concatenating string
meraNaam = 'Jai'
meraNaam_last = 'Gupta'
print(meraNaam + meraNaam_last)
print(meraNaam, meraNaam_last)

# stackoverflow

