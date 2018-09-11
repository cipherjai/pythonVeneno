# from https://realpython.com/primer-on-python-decorators/
# Functions

def add_number(number):
    return number + 3


add_number(2)

# First class object

# In Python, functions are first-class objects. This means that functions
# can be passed around and used as arguments, just like any other object
# (string, int, float, list, and so on).

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are awesome !"

def greet_bob(greeter_func):
    return greeter_func("Jai")

print(say_hello("Suraj"))
print(be_awesome("Chinu"))
print(greet_bob(say_hello))


# Inner functions
def parent():
    print("Printing from the parent () function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()

# returning functions from functions
def parent_func_return(number):
    print("Printing from the parent () function")

    def first_child():
        print("""Printing from the first_child() function
                Hi my name is Prashant """)

    def second_child():
        print("""Printing from the second_child() function
                Hi my name is Chinu """)

# only passes the reference to the function.
    if number == 1:
        return first_child
    else:
        return second_child

first = parent_func_return(1)
second = parent_func_return(2)

print(first)
print(second)

print(first())
print(second())


# the world magic is happening

def my_decorator(func):
    def wrapper():
        print("Something is happening before the fucntion is called.")
        func()
        print("Something is happening before the fucntion is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
print(say_whee())



from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22 :
            print("Shhh!!! the neighbors are Zombies!!")
            func()
        else:
            print("Shhh!!! the neighbors are dead asleep!!")
        return wrapper


def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)
print(not_during_the_night(say_whee))


# pie syntax @
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

'''@my_decorator is just an easier way of saying
say_whee = my_decorator(say_whee)
It’s how you apply a decorator to a function.'''

@my_decorator
def say_whee():
    print("Whee!")

print(say_whee)
print(say_whee())
