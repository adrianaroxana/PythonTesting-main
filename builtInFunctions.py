'''
Built-in functions in Python
'''

greet = "hello world"
print(len(greet))
print(greet[0:len(greet)])
quote = "to be or not to be"
print(quote.upper())  # capitalizes all elements of the string
print(quote.capitalize()) # capitalizes first element of the string
print(quote.find("be")) # finds first position of the string
print(quote.replace("be","me")) # replaces a string with the second one

name = "Andreea"
print(type(name))  # returns the type of data of the variable
name = 1
print(type(name))