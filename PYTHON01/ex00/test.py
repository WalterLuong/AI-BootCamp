from recipe import Recipe
from book import Book
import datetime
import time


if __name__ == '__main__':
	print(" Test ".center(42, '='), end='\n\n')
	print(" Recipe test ".center(42, '='), end='\n\n')
	print("Empty arguments ".ljust(42, '_'), end='\n\n')
	test1 = Recipe()
	print("\nInvalid arguments ".ljust(42, '_'), end='\n\n')
	test2 = Recipe(2, "oui", "non", "ketchup", False, -26)
	print("\nOne invalid arguments ".ljust(42, '_'), end='\n\n')
	test3 = Recipe("Boom", 7, 12, ["Potatoes", "Ketchup", "Mayo"], "lunch")
	print(test3)
	print("\nValid arguments ".ljust(42, '_'), end='\n\n')
	test4 = Recipe("Potatoes", 2, 12, ["Potatoes", "Ketchup", "Mayo"], "lunch", "Serve it with a burger")
	print(test4, end="\n\n")

	print(" Book test ".center(42, '='), end='\n\n')
	book1 = Book("My first recipes")
	print("First check of the book ".ljust(42, '_'), end='\n\n')
	print(book1)
	time.sleep(2)
	print("Add a recipe ".ljust(42, '_'), end='\n\n')
	book1.add_recipe(test4)
	book1.get_recipe_by_name("Potatoes")
	print()
	print("Check the book again ".ljust(42, '_'), end='\n\n')
	print(book1)
	test5 = Recipe("Burger", 4, 25, ["Burger bun", "Steak", "Cheddar", "Fried chicken, not a live chicken", "Salad", "Tomatoes", "Pickle", "Sauce"], "lunch", "Serve it with potatoes")
	time.sleep(2)
	book1.add_recipe(test5)
	book1.get_recipe_by_name("Burger")
	print()
	print("Check the book again ".ljust(42, '_'), end='\n\n')
	print(book1)