class Recipe:
	"""Class which contains all the recipes"""

	def check_args(name, cooking_lvl = 0, cooking_time = -1, ingredients = [], recipe_type = "", description = ""):
		"""Check validity of argumennts"""
		val = True
		
		if isinstance(name, str):
			if len(name) == 0:
				print("Name must be a not empty string")
				val = False
		else:
			print("Name must be a string")
			val = False
		if isinstance(cooking_lvl, int):
			if not 0 < cooking_lvl < 6:
				print("Cooking level must be an int between 1 and 6")
				val = False
		else:
			print("Cooking level must be an int")
			val = False
		if isinstance(cooking_time, int):
			if cooking_time < 0:
				print("Cooking time must be a positive int")
				val = False
		else:
			print("Cooking time must be an int")
			val = False
		if isinstance(ingredients, list):
			if len(ingredients) == 0:
				print("Ingredients must be a not empty list")
				val = False
		else:
			print("Ingredients must be a list")
			val = False
		if isinstance(recipe_type, str):
			if len(recipe_type) == 0:
				print("Recipe type must be a not empty string")
				val = False
			elif recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
				print("Recipe type must be a starter, a lunch or a dessert")
				val = False
		else:
			print("Recipe type must be a string")
			val = False
		if not isinstance(description, str):
				print("Description type must be a string")
				val = False
		return val

	def __init__(self, name = "", cooking_lvl = 0, cooking_time = -1, ingredients = [], recipe_type = "", description = ""):
		if (Recipe.check_args(name, cooking_lvl, cooking_time, ingredients, recipe_type, description)):
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.recipe_type = recipe_type
			self.description = description
		else:
			self.name = ""
	
	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt = "Invalid recipe"
		if len(self.name) != 0:
			txt = ("Recipe : " + self.name + "\n"
			+ "Cooking level: " + str(self.cooking_lvl) + "\n"
			+ "Cooking time: " + str(self.cooking_time) + " min\n"
			+ "List of ingredients: " + ', '.join(self.ingredients) + "\n"
			+ "Recipe type: " + self.recipe_type + "\n"
			+ "Description: " + self.description)
		return txt