my_list = [17, 12, 9, 3, 2]
your_list = my_list[-1]
print(your_list)
print(17 in my_list)
print(27 in my_list)


your_list = my_list[:]
your_list.append(7)
print(len(your_list))
print(len(my_list))