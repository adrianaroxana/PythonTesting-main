'''
Write a Python program to accept a filename from the user
and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
'''

filename = input("Enter filename: ")
extension = filename.split(".")
print(f"The extension of the file <{extension[0]}> is {extension[1]}")