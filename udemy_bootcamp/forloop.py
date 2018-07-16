# For Loop
lis = range(1, 10)
for numb in lis:
    if numb % 2 == 0:
        print ("Here's an even number")
    else:
        print ("Here's an odd number")
        print ("something simple")
#
# # Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.
#
# An object is called iterable if we can get an iterator from it. Most of built-in containers in Python like: list, tuple, string etc. are iterables.
#
# The iter() function (which in turn calls the __iter__() method) returns an iterator from them.

# # get an iterator using iter()
# my_iter = iter(my_list)
# if using .__next__() ,  shall raise an exception if there is no item left

# working on tuple
tup = (1,3,2,4,3,6,5)

for item in tup:
    print (item)

print("________ With Set ________")
# set
sets = {1,3,2,4,3,6,5}

for item in sets:
    print(item)

print("____________ tuple unpacking ______________")
l = [(2,3), (6,8), (10,12)]
for value in l:
    print(value)

print("___more complex tuple___")
comp_tuple = [(21,23), (23,45), (45, 34), (9, 89)]
for (t1, t2) in comp_tuple:
    print(t2)
    print(t1 + t2)

# using .iteritens to create a generate itertor to iterate through dictionary
print("___simple_dictionary___")
d = {'k1':1, 'k2':2, 'k3':3}
for k in d.items():
    print (k)
