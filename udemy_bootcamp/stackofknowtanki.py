#  1>>

## I have a tuple of tuples from a MySQL query like this:

T1 = (('13', '17', '18', '21', '32'),
      ('07', '11', '13', '14', '28'),
      ('01', '05', '06', '08', '15', '16'))
# I'd like to convert all the string elements into integers and put them back into a list of lists:

T2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]
# I tried to achieve it with eval but didn't get any decent result yet.


# accepted
# int() is the Python standard built-in function to convert a string into an integer value. You call it with a string containing a number as the argument, and it returns the number converted to an integer:

print (int("1") + 1)
The above prints 2.

# If you know the structure of your list, T1 (that it simply contains lists, only one level), you could do this in Python 2:

T2 = [map(int, x) for x in T1]
# In Python 3:

T2 = [list(map(int, x)) for x in T1]
