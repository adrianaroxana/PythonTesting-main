'''
- function to calculate the maximum out of three input numbers
- function to calculate the maximum out of three input numbers using nested functions
- define four functions to use the base mathematical operations (a calculator)
'''
from math import sqrt


def math_operations(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "**":
        return num1 ** num2
    elif operation == "rad":
        return sqrt(num1)
    else:
        return "Other operations to be added in the future."


print("Operations available: \n- + - add\n- - - subtract\n- * - multiply\n- / - division"
      "\n- ** - pow\n- rad - radical")
print(math_operations(34, 2, "+"))
print(math_operations(34, 2, "-"))
print(math_operations(34, 2, "*"))
print(math_operations(34, 2, "/"))
print(math_operations(34, 2, "**"))
print(math_operations(34, 2, "rad"))
