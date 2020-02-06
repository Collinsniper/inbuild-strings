# Built-in string functions/methods
n="HELLO"
a="hello world"
b=a.capitalize()
print(b)
print(a.capitalize()) #outputs' a string to it's first letter as a capital letter
print(a.upper()) #returns the string in upper case 
print(n.lower()) #returns the string in lower case
print(a.isupper()) # returns True if all the characters are in upper case, otherwise False.
print(n.isupper())
print(a.islower()) #returns True if all the characters are in lower case, otherwise False.
print(n.islower())
print(a.istitle()) #returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
print(b.istitle())
a = a.replace("hello", "hey") # replaces a specified phrase with another specified phrase.

print(a)
a = a.swapcase() #returns a string where all the upper case letters are lower case and vice versa.

print(a)