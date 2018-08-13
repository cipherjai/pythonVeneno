import math
import collections
import string

lamb_vol_sphere = lambda radius : math.pi * (radius ** 3)
print(lamb_vol_sphere(5))

in_the_range = lambda num, low, high: True if num >= low and num <= high else False
print(in_the_range(0, 1, 10))

def countUcLc(sentence):
    sentence.replace(" ","")
    if(len(sentence) > 0):
        count_height = 0
        count_simple = 0
        for letter in sentence:
            if(letter.isupper()):
                count_height = count_height + 1
            else :
                count_simple = count_simple + 1
        print(count_height)
        print(count_simple)

countUcLc("Whats a goo way to iterate through the string? A for loop perhaps? How can you keep track of you counts? A variable or maybe even a dictionary with a key for upper and a key for lower, then add counts to the value corresponding to the correct key.")

# *** Best Palindrome logic ***
isPalindrome = lambda stir : True if stir == stir[::-1] else False
print(isPalindrome("helleh"))

# list to set to list
lis =  [1,1,1,3,2,4,3,2,3,4,5,4,5,5]
convert_to_set = lambda lister : list(set(lister))
print(convert_to_set(lis))

# multiply
result = 1
for num in lis:
    result *= num
print(result)

# Pangram
def ispangram(str1, alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())

print(ispangram("The quick brown fox jumps over the lazy dog"))
print(string.ascii_lowercase)
