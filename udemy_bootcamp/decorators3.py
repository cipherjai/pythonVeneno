#dec 3
# functions as arguments

def hello():
    return 'H buddy'

def other(func):
    print ('Other code goes here!')
    print (func())

other(hello)


# new decorators

def new_decorator(func):

    def wrap_func():
        print ('Code here, before executing the func')
        func()
        print ('Code here will execute after the func()')

    return wrap_func

def func_needs_decorator():
    print("This function needs a decorator!")

func_needs_decorator =  new_decorator(func_needs_decorator)
func_needs_decorator()
