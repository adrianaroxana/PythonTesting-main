'''
Tuples usage definition
'''

MY_TUPLE = (1, 2, 5, 7)
print(MY_TUPLE[3])
#print(MY_TUPLE[5])
print(5 in MY_TUPLE)
print(14 in MY_TUPLE)
print(5 in MY_TUPLE)
print(MY_TUPLE.count(4))
print(MY_TUPLE.count(2))
# MY_TUPLE[0] = 5
TUP = 2, 3, 4  # if no parantheses by default it is considered to be a tuple
print(type(TUP))
print(list(TUP))
x = list(TUP)
x[0] = 3
print(x)
y = tuple(x)
print(y)
MY_TUP = (1)
print(MY_TUP)
