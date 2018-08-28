# key and a value pair
my_dict = {'key1':'value_1', 'key2':'value2'}
print(my_dict['key1'])
print(my_dict)
print(type(my_dict))
print(type(my_dict['key2']))
my_dict = {'k1':123, 'k2':3.4, 'k3':'string'}
print(my_dict['k3'][0])
print(my_dict['k3'][-1])
print(my_dict['k3'][::-1])
print(my_dict['k3'].upper())
print(my_dict['k3'])
print(type(my_dict['k3']))

my_dict['animal'] = 'Dog'
my_dict['answer'] = '42'

d = {'k1': {'nestkey': {'subnestkey': 'value'}}}
print(d['k1']['nestkey']['subnestkey'])
print((d['k1']['nestkey']['subnestkey']).upper())
print(d.keys())
print(d.values())
print(d.items())

# Iterating over dictionaries will only give you keys
