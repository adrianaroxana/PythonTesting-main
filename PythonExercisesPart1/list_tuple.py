'''Write a Python program which accepts a sequence
of comma - separated numbers from user and generate
a list and a tuple with those numbers.
'''

series = input("Enter a sequence of numbers separated by commas: ")
my_list = series.split(",")
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)