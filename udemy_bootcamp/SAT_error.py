try:
    for i in range('a', 'g'):
        print(ord(i) ** 2)
except:
    print("cannot multiply literal")

for i in range(ord('a'), ord('g')):
    print(i ** 2)


x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError as e:
    print("Can't divide by Zero")
finally:
    print("Divided")

while True:
    try:
        n = int(input("Input an Integer >"))
    except:
        print("Cannot convert literal to integer, try entering integer ")
        continue
    else:
        print("inside else block")
        print(n**2)
        break
    finally:
        print("You're a devil !")
