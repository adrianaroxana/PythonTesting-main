'''
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum.
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def add_numbers(no1, no2, no3):
    if no1 == no2 == no3:
        return 3 * no1
    else:
        return no1 + no2 + no3


print(add_numbers(a,b,c))