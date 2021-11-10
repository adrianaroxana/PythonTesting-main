'''
Write a program which will be executed by another one.
The initial program will take the username and password from
keyboard and print these variables.
The other program will check if password and username are
correct and in this case will print: "Welcome!"
Otherwise, print: "Incorect credentials. Please try again!"

Clue: Use "if/else"

!!! login.py is executed by check_login.py !!!
'''

USERNAME = input("Enter username: ")
PASSWORD = input("Enter password: ")


def login_credentials(username, password):

    '''
    This module checks if username and password are correct
    and returns the value of the authorized variable
    '''

    if username == 'Alina' and password == "abc123":
        authorized = 1
    else:
        authorized = 0
    return authorized


AUTHORIZE = login_credentials(USERNAME, PASSWORD)


if __name__ == "__main__":
    print(USERNAME)
    print(PASSWORD)
