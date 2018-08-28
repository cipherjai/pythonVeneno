# counter - Extra exercise
import collections

print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print (collections.Counter({'a':2, 'b':3, 'c':1}))
print (collections.Counter(a=2, b=3, c=1))

c = collections.Counter()
print("Initial", c)
print("sequence",c.update('abcdefgabcdefdefghghiighighi'))

c.update({'a':1, 'd':5})
print("Dict", c)
