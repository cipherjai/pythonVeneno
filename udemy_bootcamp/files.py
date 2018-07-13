f = open('merelysimpledoc.txt')
print(f.read())
f.seek(0)
print(f.readlines())
print(type(f.readlines()))

for line in open('merelysimpledoc.txt'):
    print line
