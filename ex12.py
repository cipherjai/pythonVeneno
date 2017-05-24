from sys import argv
#This is how to add features from the python feature set.
#Add only what you plan to use
#acts as a documentation

#argv is the argument variable
#holds the arguement you pass to your python script whenever you run it

#it unpacks the arguments
script, first, second, third, philly = argv


print(first + second + third)

print("Welcome to %s" % philly)
print("The script is called : " + script)
print("Your first variable is : " + first)
print("Your second variable is : " + second)
print("Your third variable is : " + third)






