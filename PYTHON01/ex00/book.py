from recipe import Recipe
import datetime

class Book:
	
	def __init__(self, name = ""):
		if isinstance(name, str):
			self.name = name
		else:
			print("Name must be a string")
		self.last_update = datetime.datetime.today().replace(microsecond=0)
		self.creation_date = datetime.datetime.today().replace(microsecond=0)
		self.recipes_list = {'starter' : [], 'lunch' : [], 'dessert' : []}

	def __str__(self):
		"""Print all the informations about the book"""
		starters = []
		for k in self.recipes_list['starter']:
			starters.append(k.name)
		lunches = []
		for l in self.recipes_list['lunch']:
			lunches.append(l.name)
		desserts = []
		for m in self.recipes_list['dessert']:
			desserts.append(m.name)

		text = ("Book's name: " + self.name + '\n'
		+ "Created at " + str(self.creation_date) + '\n'
		+ "Last updated at " + str(self.last_update) + '\n'
		+ "Starters: " + str(starters) + '\n'
		+ "Lunches : " + str(lunches) + '\n'
		+ "Dessert : " + str(desserts) + '\n')
		return text

	def get_recipe_by_name(self, name):
		"""Prints a recipe with the name \texttt{name} and returns the instance"""
		if isinstance(name, str):
			for recipes in self.recipes_list.values():
				for r in recipes:
					if r.name == name:
						print(r)
						return r
			print("This recipe is not in the book.")
		else:
			print("Name must be a string.")

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type"""
		if isinstance(recipe_type, str):
			if recipe_type == 'starter' or recipe_type == 'lunch' or recipe_type == 'dessert':
				print(recipes_list[recipe_type])
			else:
				print("Recipe type must be a starter, a lunch or a dessert")
		else:
			print("Recipe type must be a sting")

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if not isinstance(recipe, Recipe):
			print("You must add a recipe")
		else:
			self.recipes_list[recipe.recipe_type].append(recipe)
			self.last_update = datetime.datetime.today().replace(microsecond=0)