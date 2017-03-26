# Revising all until this point

# 1 console printing
print("Hello World!")
print("Hello's World")
print("So printing ' ' inside \" \" is all right !")
print('does it print inside a single quote \' a single quote again? ')

# 2 commenting and multi line commenting
''' Multi Line commenting is possible now
and you know what , you are not made to love anybody'''
print("just checking whether the", "works for the two strings in here ?")
# adds a space automatically after there's a comma

# 3 Maths
print("Hearts:", 27 + 35)
print("Check how truth said ", 27 > 35)
''' In the United States we use an acronym called P E M D A S which stands for
Parentheses Exponents Multiplication Division Addition Subtraction.
That's the order Python follows as well. '''

print("What is #3+2")
# #3+2
print('What is #3+2')
# #3+2
print("What is 3+2?", 3 + 2)
# 5

# 4 Variables
print("The change is here: ")
stringOnGuitar = 6
totalNumberOfFrets = 20
numberOfFingersRequired = 4
totalNumberOfTriads = 21
beatMeasure = 4
fireWorks = True
melodyRhythm = False
theBasicChord = 'C Major'
theMostAwesomeTuning = "Open D"
theMostFavoriteSong = "Titanic's Theme"
theVariantBetweenTheNotes = 2.54
# capital Letters can be used to name a variable
BOLDog = 'Do not use it'
# Multiplying
print(stringOnGuitar)
print(totalNumberOfFrets * theVariantBetweenTheNotes)
print(totalNumberOfFrets * theVariantBetweenTheNotes + numberOfFingersRequired)
print(fireWorks + 1)
print(melodyRhythm + 1)
print(fireWorks - 1)
# print(fireWorks + theBasicChord)
# print("In guitar, we have total number of  notes" &(stringsOnGuitar*totalNumberOfFrets))
# ** Discovered something new here **
newVariable = stringOnGuitar, theBasicChord, "100" * 10
print(newVariable)

# 5 formatted or unformatted
# embedding
myName = 'Jai'
myAge = 23
myHeight = 165.67
myWeight = 65
print("My Name is %s !" % myName)
print("I'm %f cm tall" % myHeight)
print("I'm %f heavy" % myWeight)
print('I think it does\'t prints the formats here like my age is %d ' % myAge)
print("But it prints in here %d")
print("I also said  %r" % myName)

# 7 Printing weird
print("It's fleet was white as %s" % 'snow')

# 8 Formatting the mater debugger
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % (formatter, formatter, formatter, formatter))

# 9 Printing more strings
print(""" The multi-line printer is here now
without the problem of going along in one line """)
print("""Also, in triple quotes , there is no need of using escape sequences for printing " or "" , chill """)

# 10 Escape Sequences
# escape sequences
# Escape	What it does.
# \\	Backslash (\)
# \'	Single-quote (')
# \"	Double-quote (")
# \a	ASCII bell (BEL)
# \b	ASCII backspace (BS)
# \f	ASCII formfeed (FF)
# \n	ASCII linefeed (LF)
# \N{name}	Character named name in the Unicode database (Unicode only)
# \r	Carriage Return (CR)
# \t	Horizontal Tab (TAB)
# \uxxxx	Character with 16-bit hex value xxxx (u'' string only)
# \Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (u'' string only)
# \v	ASCII vertical tab (VT)
# \ooo	Character with octal value ooo
# \xhh	Character with hex value hh

# 11 Input From User
print("How Old are You ?"),
# adding , after the print sentence is good enough
age = int(input())  # type casting to integer , to string .. we use str()
print("Your age is %d" % (age + 1))
# %r is for debugging
color = input("What is your Favourite colour baby ?"),
shade = input("What eye-shades do you use ? "),
cars = input("Which car do you have ? "),

# 12 argv
from sys import argv
script, one, two, three = argv
print("Yay tha kya ? ", script, one, two, three, " I know , lol!")

# 15 Reading A File
someFile = open(one)
print("Here is your bloody file %r: " % one)
print(someFile.read())
someFile.close()

# 16 More play with the file
print("We're going to erase %r." % one)
print("If you don't want this to happen, press Ctrl + C (^C) .")
print("Enter if you agree!")
input("?")
print("Opening File.....")
target = open(one, 'w')
# There are different modes by which we can open the files in different modes
print("Truncating the file ---- Say Goodbye !")
target.truncate()
print("Now, a file shouldn't be empty, Enter something into it !")
line1 = input("Line One : "),
line2 = input("Line Two : "),
line3 = input("Line Three : "),
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
print("And finally we close it down")
target.close()
# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)
