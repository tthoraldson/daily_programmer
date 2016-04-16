# Daily Programmer - Easy Challenge 005
# Completed on 4/15/2016 by Theresa Thoraldson

username = "Theresa" #correct username
password = "coolbeans@31" #correct password

susername = input("Username: ") #user input username
spassword = input("Password: ") #user input password

print() #space
if susername == username and spassword == password:
	print("Access granted.") #if username and password are correct
else:
	print("Access denied.") #if username and/or password are incorrect