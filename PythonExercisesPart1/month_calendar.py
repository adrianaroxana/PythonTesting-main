'''
Write a Python program to print the calendar of a given month and year.

Note: Use 'calendar' module.

Python calendar.month(theyear, themonth, w=0, l=0):

The function returns a month’s calendar in a multi-line string using
the formatmonth() of the TextCalendar class.

'l' specifies the number of lines that each week will use.
'''

import calendar


y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
print(calendar)