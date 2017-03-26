from sys import argv
from os.path import exists

script, fromFile, toFile = argv
print("Copying from file %s to file %s" % (fromFile, toFile))

inFile = open(fromFile, 'w')
inData = fromFile.read()

print("The input file is %d bytes long! " % (len(inData)))
print("Does output file %s exists ? %r " % (toFile, exists(toFile)))

input()
outFile = open(toFile,'w')
outFile.write(inData)
print("All Done. Now closing all stuff")
outFile.close()
inFile.close()
