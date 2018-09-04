# enumerate the list items to refer them easily

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(type(enumerate(l)))

for count, obj in enumerate(l):
    print(count, obj)

# other uses of enum

for count, obj in enumerate(l):
    if count >= 2 :
        break

    else:
        print(obj)

# s = 'abcdefghijklmnopqrstuvwxyz'
# x = ""
# for i in s:
#     x += ("'" + i + "', ")
#
# print(x)

# New comment
