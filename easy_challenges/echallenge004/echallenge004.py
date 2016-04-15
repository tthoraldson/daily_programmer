# Daily Programmer - Easy Challenge 004
# Completed on 4/15/2016 by Theresa Thoraldson 

import random
import string

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' , 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*'] #list of random characters for the passwords

lengthstring = input("how many characters would you like in your random passowrd?")
length = int(lengthstring) #how long the generated passwords will be

pass_string = input("how many passwords would you like to generate?")
pass_am = int(pass_string) #how many passwords will be generated
print() #line break

for password in range(pass_am):
	print(''.join(random.choice(list) for I in range(length)))
