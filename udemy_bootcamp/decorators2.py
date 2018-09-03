# def hello(name = 'Jose'):
#
#     print("The hello() function has been executed")
#
#     def greet():
#         return '\t this is inside the greet function'
#
#     def welcome():
#         return '\t This is inside the welcome()'
#
#     print(greet())
#     print(welcome())
#     print("Now we are back inside the hello function")
#
# print(hello())
# print(welcome())


# now not returning the actual functions

def hello(name = 'Jose'):

    print("The hello() function has been executed")

    def greet():
        return '\t this is inside the greet function'

    def welcome():
        return '\t This is inside the welcome()'

    if name == 'Jose':
        return greet
    else:
        return welcome

    print(greet())
    print(welcome())
    print("Now we are back inside the hello function")

x = hello()
print(x)
print (x())
