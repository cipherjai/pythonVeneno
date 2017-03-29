#formatted Strings
# ""

# denotes a format sequence inside a string
myEyes = 'Blue'
myNose = 'Beautiful'
myLips = 'Rosy'
mySmile = 'Killing'
meriAdaa = 'sufi'

myAge =22
myHeight = 56
myName = "Awesome"

print('Let\'s talk about Mr. %s' %myName)
print("Let's talk about Mr. %s" %myName)

print('My height is %d inches' %myHeight)
print("My height is %d inches" %myHeight)

#Multiple Formats

print("If i add #myAge =%d & #height =%d, I'll get - %d" %(myAge,myHeight,myAge+myHeight))
print("My Eyes are : ",myEyes,"and my nose is %s" %myNose)
print('My height is perfectly %d inches tall' %(myHeight*2.54))
print(myEyes+myLips+'are sexy enough')

myHeight = 6 * meriAdaa
print(myHeight)

print(7/4)
print(round((1.499)))


# Character Play

mera_naam = "Jai Gupta"
print(mera_naam[0])
print(mera_naam[6])

# computers start counting from 0
# there is no negative zero ! Don't laugh but look at this

print(mera_naam[-1])
# therefore it prints the last character

# ranging with the characters
print(mera_naam[1:7])

# ranging without beginnning
print(mera_naam[:7])
# print the whole fro starting

# finding lengths
print(len(mera_naam))
