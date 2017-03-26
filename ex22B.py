# 17 multiple files
from sys import argv
from os.path import exists

script, fromFile, toFile = argv
print("Copying from file %s to file %s" % (fromFile, toFile))

inFile = open(fromFile)
inData = inFile.read()

print("The input file is %d bytes long! " % (len(inData)))
print("Does output file %s exists ? %r " % (toFile, exists(toFile)))

input()
outFile = open(toFile, 'w')
outFile.write(inData)
print("All Done. Now closing all stuff")
outFile.close()
inFile.close()


# 18 Arguments and Def Functions
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))
    outFile = open(toFile, 'w')
    outFile.write(arg1 + " " + arg2)
    outFile.close()


def single():
    print("bhi nai hai mere pass")

single()
print_two('I love you', "Twinkle")


# 19 More Functions and variable
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("And we can combine the two, variables and math:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# 20 Seeking a FIle
def printAll(f):
    print(f.read())


def rewind(f):
    f.seek(0)


def print_a_Line(linecount, f):
    print(linecount, f.readLine())


currentFile = open(toFile)
print("First let's print the whole file: \n")
printAll(currentFile)
