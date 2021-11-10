a = [1, 2, 3]
b = ["bananas", "apples", "quinces", "apples"]
c = [4, "grapes", True]
print(a)
print(b)
print(c)
print(a, b, c)
print("First element of each list is:", a[0], b[0], c[0])
# Homework: print with format

print(a[2], b[2], c[2])
print(a[-1], b[-1], c[-1])
print(a[0:2])
print(b.count("apples")) # counts the occurences of the element
c[-1] = "oranges" #replaces an element of the list
print(c)
print(sum(a))
print(a.clear())
a.append(4)
print(a)
print(3 in a) # checks if element is in list
