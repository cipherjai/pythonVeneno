from sys import argv
from os.path import exists

script, fromFile, toFile = argv
print("Copying from %s to %s"%(fromFile, toFile))

inFile = open(fromFile)
inData = fromFile.read()

print("The input file is %d bytes long!" %(len(inData)))

print("Does the output file exists? %r" %exists(toFile))
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

outFile = open(toFile,'w')
outFile.write(inData)
print("Alright, all done.")

outFile.close()
inFile.close()
