'''
Define a username getting input from the console
Define a password getting input from the console
Display the following message:
'The password for user Andrew is *********
and it is 9 characters long
'''

username = input("Enter username: ")
password = input("Enter password: ")
cripted_password = ''
i = 0
for char in password:
    cripted_password += '*'
    i += 1

print(f'The password for user {username} is {cripted_password} and is {len(cripted_password)} characters long')


