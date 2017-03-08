from sys import argv

script, inputFile = argv

def printAll(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_Line(lineCount, f):
    print(lineCount, f.readLine())

currentFile = open(inputFile)

print("First let's print the whole file: \n")

