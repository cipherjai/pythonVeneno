#READING A FILE IN PYTHON
from sys import argv

script, fileName = argv
txt =  open(fileName)

print("here is your file %r:" %fileName)
print(txt.read())
txt.close()
print("Type the fileName again: ")
fileAgain = input("> ")
txtAgain = open(fileAgain)

print(txtAgain.read())
txtAgain.close()

