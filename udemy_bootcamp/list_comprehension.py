l = []
lc = [x for x in 'chinu']

for letter in lc:
    print(lc)
    print(type(lc))
    l.append(letter)

print(l)

# comprehension
l = [letter for letter in 'Prashant']
print(type(l))
print(l)

l = [x**2 for x in range(0, 11)]
print(l)

l = [number for number in range(11) if (number % 2 == 0)]
print(l)

l = []
for number in range (11):
    if number % 2 == 0 :
        l.append(complex(number))
print(l)


celsius = [0, 10, 20.1, 34.5]

fahrenheit = [temp * 1.8 for temp in celsius]
print(list(fahrenheit))

fahrenheit = [(temp * (9/5.0)+32) for temp in celsius]
print(fahrenheit)

l = [x ** 2 for x in [x ** 2 for x in range(11)]]
print(l)
