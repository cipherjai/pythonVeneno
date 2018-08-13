#unordered -  means no indexing
#unique
# dictionaries with only keys that are unique
x = set()
print(type(x))

x.add("Something")
print(x)
x.add("otherthing")
print(x)
x.add(34)
print(x)
x.add(345.5)
print(x)
x.add(34)
print(x)

l = [1,2,3,4,5,6,7,8,1,3,5,6,8,3,5,6,4,3,5,5,5,3,22,3,45,56,45,56,10,10]
print(l)
print(set(l))
print("is a list ", list(set(l)))
print(sorted(set(l)))

#booleans
a = True
print((1>2)<(2>1))
b = None
print(b)
b = 'a'
print(b)
