'''
Checks the login module
'''

import login


while login.AUTHORIZE == 0:
    print("Please try again")
    login.USERNAME = input("Enter username: ")
    login.PASSWORD = input("Enter password: ")
    login.AUTHORIZE = login.login_credentials(login.USERNAME, login.PASSWORD)


print("You are authenticated")
