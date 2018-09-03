def func():
    return 1

print(func())

s = 'This is a global variable'

def func():
    print (locals())

func()
print(globals().keys)
print(globals()['s'])

 def hello(name = 'Jose'):
     return 'Hello '+name

hello()
'Hello Jose'
greet = hello

greet()

del hello

greet()
