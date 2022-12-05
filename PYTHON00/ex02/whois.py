import sys

number = 0

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")

elif not sys.argv[-1].isdigit() and (sys.argv[-1][0] != '-' and sys.argv[-1][0] != '+'):
	print("AssertionError: argument is not an integer")

else:
	number = int(sys.argv[-1])
	if (number == 0) :
		print("I'm Zero.")
	elif number % 2 == 0 :
		print("I'm Even.")
	else:
		print("I'm Odd.")