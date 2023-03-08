class GotCharacter:
	"""\033[1;3mA random GoT character, nobody knows what will happen to him.\033[m"""
	def __init__(self, first_name=None, is_alive=True) -> None:
		if isinstance(first_name, str):
			self.first_name = "\033[1;33m" + first_name + "\033[m"
		if isinstance(is_alive, bool):
			self.is_alive = is_alive

	def __str__(self) -> str:
		if self.is_alive:
			txt = ("I am \033[1;32malive\033[m and my name is " + self.first_name)
		else:
			txt = ("I am \033[1;31mdead\033[m and my name is " + self.first_name)
		return txt

class Stark(GotCharacter):
	"""\033[1;3mA class representing the Stark family. Or when bad things happen to good people.\033[m"""
	def __init__(self, first_name=None, is_alive=True) -> None:
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "\033[1;33mStark\033[m"
		self.house_word = "\033[3;34mWinter is coming\033[m"

	def __str__(self) -> str:
		return super().__str__() + " " + self.family_name + ", my house word is: " + self.house_word
	
	def print_house_words(self) :
		print(self.house_word)

	def die(self):
		self.is_alive = False

class lannister(GotCharacter):
	"""\033[1;3mA class representing the Lannister family. Money lovers.\033[m"""
	def __init__(self, first_name=None, is_alive=True) -> None:
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "\033[1;33mLannister\033[m"
		self.house_word = "\033[3;34mA lannister always pays his debts\033[m"

	def __str__(self) -> str:
		return super().__str__() + " " + self.family_name + ", my house word is: " + self.house_word
	
	def print_house_words(self) :
		print(self.house_word)

	def die(self):
		self.is_alive = False

if __name__ == '__main__':
	Walter = GotCharacter("Walter")
	RandomGuy = GotCharacter("Random", False)
	arya = Stark("Arya")
	cersei = lannister("Cersei", False)
	print(Walter)
	print(RandomGuy)
	print(arya)
	print(cersei)
	arya.print_house_words()
	arya.die()
	cersei.print_house_words()
	print(arya)
	print(arya.__doc__)
	print(Walter.__doc__)
	print(cersei.__doc__)

