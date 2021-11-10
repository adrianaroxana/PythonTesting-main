'''
Build a program to calculate the followings using the input from the user for a, b, c or r
*triangle area using input
*rectangle area and perimeter
*circle area
'''

print("foo\'bar")
#triangle area
triangle_base = float(input("Enter the length of the base of the triangle: "))
triangle_height = float(input("Enter the length of the height of the triangle: "))
triangle_area = 1/2 * triangle_base * triangle_height
print(f'The triangle area is {triangle_area}')


#rectangle area
rectangle_l = float(input("Enter rectangle length: "))
rectangle_w = float(input("Enter rectangle width: "))
rectangle_area = rectangle_w * rectangle_l

#rectangle perimeter
rectangle_p = 2 * (rectangle_w + rectangle_l)

print(f'The area of the rectangle is {rectangle_area} and the rectangle perimeter is {rectangle_p}')


#circle area
PI = 3.14
r = float(input('Enter circle radius: '))
circle_area = PI * r**2
print(f'The area of the circle is {circle_area}')