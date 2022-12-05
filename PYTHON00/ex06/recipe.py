# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:09:43 by wluong            #+#    #+#              #
#    Updated: 2022/12/05 05:09:45 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
	print("\033[1;33mYou have the following recipees:\033[m")
	for k in cookbook:
		print("\033[3;33m\t%s\033[m" % k)

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
		name = input('\033[1;35m>>> Enter a name: \n\033[m')
		if name:
			break
	print("\033[1;35m>>> Enter ingredients:\033[m")
	ingredients = []
	while True:
		new = input()
		if not new and len(ingredients) > 0:
			break
		elif new:
			ingredients.append(new)
		else:
			print("\033[1;31mYou should have at least 1 ingredient.\033[m")
	while True:
		meal = input("\033[1;35m>>> Enter a meal type: \n\033[m")
		if meal:
			break
	print("\033[1;35m>>> Enter a preparation time:\033[m")
	while True:
		prep_time = input()
		if not prep_time:
			print("\033[1;31mPlease enter the time.\033[m")
		elif not prep_time.isdigit():
			print("\033[1;31mThe time must bean integer.\033[m")
		else:
			break

	updated_cookbook = { name : {
		'ingredients' : ingredients,
		'meal' : meal,
		'prep_time' : int(prep_time) }}

	cookbook.update(updated_cookbook)


if __name__=="__main__":
	print("\033[1;4;32mWelcome to the Python Cookbook !\033[m")
	while True:
		print ("\033[3m\nList of available option:\n\n" + "\t1: Add a recipe\n" + "\t2: Delete a recipe\n" + "\t3: Print a recipe\n" + "\t4: Print the cookbook\n" + "\t5: Quit\n\033[m" )
		print("\033[1;34mPlease select an option:")
		option = input(">> \033[m")
		print("")
		if not option:
			print("\033[1;31mYou must enter an option.\033[m")
		elif not option.isdigit() or int(option) > 5:
			print("\033[1;31mSorry, this option does not exist.\033[m")
		elif int(option) == 1:
			add_recipe()
		elif int(option) == 2:
			delete = input("\033[1;34mEnter the recipe you want to delete:\n>>> \033[m")
			remove_recipe(delete)
		elif int(option) == 3:
			details = input("\033[1;34mPlease enter a recipe name to get its details:\n>>> \033[m")
			print_recipe_detail(details)
		elif int(option) == 4:
			print_recipees()
		elif int(option) == 5:
			print("\033[1;5;4;31mCookbook closed. Goodbye\033[m")
			break