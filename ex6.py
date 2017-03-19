''' dum = 2
x = "There are %d types of people",dum
# Answer= ('There are %d types of people', 2)
print (x)

x = "There are %d types of people"
binary = "binary"
doNot = "don't"
y =  "ZThose who know %s and those who %s." %(binary, doNot)


print (x)
print (y)

#
# The %s specifier converts the object using str(), and %r converts it using repr().
#
# For some objects such as integers, they yield the same result, but repr() is special in that (for types where this is possible) it conventionally returns a result that is valid Python syntax, which could be used to unambiguously recreate the object it represents.
#
# Here's an example, using a date:
#
# >>> import datetime
# >>> d = datetime.date.today()
# >>> str(d)
# '2011-05-14'
# >>> repr(d)
# 'datetime.date(2011, 5, 14)'


print ("I said: %r.")%(x)
print ("I also said: '%s'.") %(y)

hilarious = False
jokeEvaluation = "Isn't that joke funny? ! %r"

w = "This is the left side of ..."
e = "a string with a right side."

print (w+e)
'''
# ###########################

x = "There are %d types of people." %(10)
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
