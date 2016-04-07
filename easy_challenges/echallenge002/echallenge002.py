# Daily Programmer - Easy Challenge 002
# Completed on 4/7/2016 by Theresa Thoraldson
import math

print("Welcome to Theresa's pythagorean theorem solver 1.0!")

x = input("Are you trying to find the hypotenuse of a right sided triangle? (y/n)")
if x=='y':
	#finding the hypotenuse in a right sided triangle
	print("Please enter the values for 'leg 1' and 'leg 2'")

	astring = input('leg 1 = ') #value for leg a
	a = int(astring)

	bstring = input('leg 2 = ') #value for leg b
	b = int(bstring)

	print()
	print("The value of hypotenuse is:")
	print(math.sqrt((a*a)+(b*b)))

elif x=='n':
	#finding a leg in a right sided triangle
	print("Please enter the values for the leg and hypotenuse of a right sided triangle")
	
	leg_string = input('leg = ')
	leg = int(leg_string)

	hyp_string = input('hypotenuse = ')
	hyp = int(hyp_string)
	
	print()
	print("The value of the second leg is:")
	print(math.sqrt((hyp*hyp)-(leg*leg)))
	
else:
	print("Error! Please respond using 'y' or 'n'")