def max_of_list(my_list):
    max = my_list[0]
    for element in my_list:
        if element > max:
            max = element
    return max

myList = []
i = 0
while i < 10:
    myList.append(int(input("Enter an element in list: ")))
    i += 1

print(myList)
x = max_of_list(myList)
print(f"The maximum of the list is {x}")
