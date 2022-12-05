import sys

arguments = ""
final_string = ""

for str in sys.argv[1::]:
	arguments += str
	if str != sys.argv[-1] :
		arguments += " "


for letter in arguments[::-1]:
	if (letter.isupper()):
		final_string += letter.lower()
	elif (letter.islower()):
		final_string += letter.upper()
	else:
		final_string += letter


print(final_string)