import random

def generator(text, sep=" ", option=None):
	"""The function called generator that takes a text as input (only printable characters), uses the string parameter sep as a splitting parameter, and yields the resulting substrings."""
	words = text.split(sep)
	if option == "ordered":
		words.sort()
	elif option == "unique":
		words = [word for n, word in enumerate(words) if word not in words[:n]]
	elif option == "shuffle":
		for i in range(len(words) - 1, 0, -1):
			j = random.randint(0, i)
			tmp = words[i]
			tmp2 = words[j]
			words[i], words[j] = tmp2, tmp
	for x in words:
		yield x

if __name__ == '__main__':
	text = text = "Le Lorem Ipsum est simplement du faux texte. est est test texte. ok mec Salut"
	print("\nNORMAL TEST ".ljust(42, "_"), end="\n\n")
	for x in generator(text):
		print(x)
	print("\nSHUFFLE TEST 1 ".ljust(42, "_"), end="\n\n")
	for x in generator(text, " ", "shuffle"):
		print(x)
	print("\nSHUFFLE TEST 2 ".ljust(42, "_"), end="\n\n")
	for x in generator(text," ", "shuffle"):
		print(x)
	print("\nORDERED TEST ".ljust(42, "_"), end="\n\n")
	for x in generator(text," ", "ordered"):
		print(x)
	print("\nUNIQUE TEST ".ljust(42, "_"), end="\n\n")
	for x in generator(text," ", "unique"):
		print(x)