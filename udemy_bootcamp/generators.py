'''
Iterators vs Generators

> Allows us to write a function which can send back a value and later resume to pick up where it left off
> Generators use yield


'''

def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print (x)


def generateFibonacci(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        # temp = a
        # a = b
        # b = temp + b
        a,b = b, a+b

for num in generateFibonacci(10):
    print(num)

def simple_gen():
    for x in range(3):
        yield x

    g = simple_gen()
    print next(g)

s_iter = iter(s)

print(next s_iter)
