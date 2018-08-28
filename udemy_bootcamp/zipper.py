# mixes them up and provide with the tuples

x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x,y)))

a = [1, 2, 3, 4, 5]
b = [2, 2, 10, 1, 1]

for pair in zip(a,b):
    print(max(pair))

map(lambda pair: max(pair), zip(a,b))

x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
print(list(map(lambda pair: max(pair), zip(x, y))))

print(zip(x, y))

# iterating over dictionaries shall only give you keys

d1 = {'a':2, 'b':5}
d2 = {'a':4, 'b':8}
zip(d1, d2)

for i in d1 :
    print(i)

print(list(zip(d2.values(), d1.values())))

# switching values
def switcher(d1, d2):
    dout = {}
    for d1K, d2V in zip(d1, d2.values()):
        dout[d1K] = d2V

    return dout

print((switcher(d1, d2)))
