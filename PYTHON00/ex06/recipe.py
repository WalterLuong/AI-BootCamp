# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:09:43 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 04:03:04 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from simple_colors import *

cookbook = {

	'Sandwich' :
	{
		'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
		'meal' : 'lunch',
		'prep_time' : 10,
	},

	'Cake' :
	{
		'ingredients' : ["flour", "sugar", "eggs"],
		'meal' : 'dessert',
		'prep_time' : 60,
	},

	'Salad' :
	{
		'ingredients' : ["avocado", "arugula", "tomatoes", "spinach"],
		'meal' : 'lunch',
		'prep_time' : 15,
	},

}

def print_recipees():
	print(yellow("You have the following recipees:", 'bold'))
	for k in cookbook:
		print(yellow("\t%s" % k, 'italic'))

def print_recipe_detail(name):
	for k in cookbook:
		if k == name:
			print("Recipe for %s:" % k)
			print("\tIngredients list: ", cookbook.get(k).get('ingredients'))
			print("\tTo be eaten for %s." % cookbook.get(k).get('meal'))
			print("\tTakes %d minutes of cooking." % cookbook.get(k).get('prep_time'))
			return
	print("Recipe not found.")

def remove_recipe(name):
	for k in cookbook:
		if k == name:
			del cookbook[k]
			return
	print("The recipe does not exist.")

def add_recipe():
	
	while True:
		name = input(magenta('>>> Enter a name:', 'bold'))
		if name:
			break
	print(magenta(">>> Enter ingredients:", 'bold'))
	ingredients = []
	while True:
		new = input()
		if not new and len(ingredients) > 0:
			break
		elif new:
			ingredients.append(new)
		else:
			print(red("You should have at least 1 ingredient.", 'bold'))
	while True:
		meal = input(magenta(">>> Enter a meal type: \n", 'bold'))
		if meal:
			break
	print(magenta(">>> Enter a preparation time:", 'bold'))
	while True:
		prep_time = input()
		if not prep_time:
			print(red("Please enter the time.", 'bold'))
		elif not prep_time.isdigit():
			print(red("The time must bean integer.", 'bold'))
		else:
			break

	updated_cookbook = { name : {
		'ingredients' : ingredients,
		'meal' : meal,
		'prep_time' : int(prep_time) }}

	cookbook.update(updated_cookbook)


if __name__=="__main__":
	print(green("Welcome to the Python Cookbook !",['bold', 'underlined']))
	while True:
		print ("\033[3m\nList of available option:\n\n" + "\t1: Add a recipe\n" + "\t2: Delete a recipe\n" + "\t3: Print a recipe\n" + "\t4: Print the cookbook\n" + "\t5: Quit\n\033[m" )
		print(blue("Please select an option:", 'bold'))
		option = input(blue(">> ", 'bold'))
		print("")
		if not option:
			print(red("You must enter an option.", 'bold'))
		elif not option.isdigit() or int(option) > 5:
			print(red("Sorry, this option does not exist.", 'bold'))
		elif int(option) == 1:
			add_recipe()
		elif int(option) == 2:
			delete = input(cyan("Enter the recipe you want to delete:\n>>> ", 'bold'))
			remove_recipe(delete)
		elif int(option) == 3:
			details = input(cyan("Please enter a recipe name to get its details:\n>>> ", 'bold'))
			print_recipe_detail(details)
		elif int(option) == 4:
			print_recipees()
		elif int(option) == 5:
			print(red("Cookbook closed. Goodbye.", ['underlined', 'bold']))
			break