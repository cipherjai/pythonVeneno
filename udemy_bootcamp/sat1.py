st = 'Print only the words that start with s in this sentence'
sent = st.split(' ')
print(sent)
li = [word for word in sent if word[0] == 's']
print(li)


# storee = range(0, 11, 2)
storee = [number for number in range(0, 11) if number%2 == 0]
print(storee)

st = 'Create a list of the first letters of every word in this string'
str = st.split(' ')
sent = [word[0] for word in str]
print(sent)

licie = []
for number in range (1, 101):
    if(number % 3 == 0 and number % 5 == 0):
        licie.append("fizzbuzz")
    elif(number % 3 == 0):
        licie.append("fizz")
    elif(number % 5 == 0):
        licie.append("buzz")
    else:
        licie.append(number)

print(licie)
