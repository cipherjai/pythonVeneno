my_list = [1, 2, 3]
print(my_list[2])
print(len(my_list))

#indexing and slicing
my_list = ['one', 'two', 'three', 4, 5]
print(my_list[1:])
print(my_list[2:])
print(my_list[:])
print(my_list[:4])
print(my_list[2:5])
print(my_list[2:6])

print(my_list*2)

my_list += ['added one']
print(my_list)

my_list.append("Quit it")
print(my_list)

new_list = ['a', 'e', 'x', 'b', 'c']
newly_list = (list(reversed(new_list)))
print(newly_list)
print(list(sorted(newly_list)))

new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)

l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = [l_1, l_2, l_3]
print(matrix)

print(matrix[0][2])
print(matrix[1][1])
print(matrix[2][0])
