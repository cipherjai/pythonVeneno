def print_two(*args):
    arg1, arg2 =args
    print("arg1: %r, arg2: %r" %(arg1,arg2))


def printTwoAgain(arg1,arg2):
    print("arg1: %r, arg2: %r" %(arg1,arg2))

def print_one(arg1):
        print("arg1: %r" % arg1)

def print_none():
    print ("I got Nothing")

print_two("Zed","Shaw")
printTwoAgain("Zed","Shaw")
print_one("First!")
print_none()

'''
7
down vote
accepted
In python the default return value of a function is None.

>>> def func():pass
>>> print func()     #print or print() prints the return Value
None
>>> func()           #remove print and the returned value is not printed.
>>>
So, just use:

letter_grade(score) #remove the print

Another alternative is to replace all prints with return:

def letter_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return  "C"
    elif 60 <= score <= 69:
        return "D"
    elif score < 60:
        return "F"
    else:
        #This is returned if all other conditions aren't satisfied
        return "Invalid Marks"
Now use print():

>>> print(letter_grade(91))
A
>>> print(letter_grade(45))
F
>>> print(letter_grade(75))
C
>>> print letter_grade(1000)
Invalid Marks
'''
