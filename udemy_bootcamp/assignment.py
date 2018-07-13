d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(type(d))
print(type(d['k1']))
print(type(d['k1'][0]))
print(type(d['k1'][0]['nest_key']))
print(type(d['k1'][0]['nest_key'][1]))
print(type(d['k1'][0]['nest_key'][1][0]))
print(d['k1'][0]['nest_key'][1][0])

newd = {'k1':[1,2,{'k2':['this is tricky', {'toughie':[1,2,['hello']]}]}]}
print(type(newd))
print(type(newd['k1']))
print(newd['k1'][2]['k2'][1]['toughie'][2][0])


# Solution

print(2/3)
print(abs(2/3))
print(2.0/3)
print(4.0 * (6+5))

stringer = "Hello World"
print(stringer.swapcase())
print(stringer.capitalize())
print(stringer.title())
# stringer[0] = 'J'

# cannot be reassigned

sentence = "Theres a huge monster ! God Save me :\("
print(sentence)
print(sentence.split(' '))
print(sentence.count('e'))

# Ranging a list
l = range(10)
print(l)
print(l[::2])
print(l[1:2:3])
print(l[::-1])

a = range(4)
print(type(a))

zero_list = [0]*3
print(zero_list)

# list can be mutated
l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print(l)


# dictionary cannot be sorted
# because they are mapping
# store as hash indexes

dictator = {}

# tuple
t = (1,2,3)

# set {}

# TODO: find out when to use [:::] and how it performs
# TODO: find out how does slicing happens
