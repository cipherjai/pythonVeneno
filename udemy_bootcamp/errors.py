# Errors or Exception

# try and Except
# code into try
# except for handling errors

# Try except finally

try:
    2 + 's'
except TypeError:
    print ("There was a type error!")
finally:
    print ("In Finally Block")

# opening a file

try:
    f = open('testfile', w)
    f.write('Test write')
except:
    print('Error in writing to the file!')
else:
    print('File write was a successful')
    f.close()

# Finally Block
try:
    f = open('testfile.txt', 'w')
    f.write('Test write this')
except:
    print("There was an error !!")
finally:
    print("Inside finally block which always executes !!")

# try except Finally

def askint():
    while True:
        try:
            val = int(input('Please provide an integer > '))
        except:
            print("Looks like you did not enter an integer")
            continue
        else:
            print("Correct, thats's an integer")
            break
        finally:
            print("Finally block executed")
        print (val)

askint()
