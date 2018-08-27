# map

def fahrenheit(temperature):
    return (9.0/5)*temperature + 32

print(fahrenheit(23))

list_of_celsius = [22.4, 45.03, 12.45, 0.4]
print(list (map(fahrenheit, list_of_celsius)))

# using lambda

print(list(map(lambda T: (9.0/5)*T + 32 , list_of_celsius)))

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print(list(map((lambda x,y,z : x+y+z), a, b, c)))
print(list(map((lambda x, y, z: x**2+y**3+z**0.5), a, b, c)))
