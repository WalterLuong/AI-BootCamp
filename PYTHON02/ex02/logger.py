# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:19:28 by wluong            #+#    #+#              #
#    Updated: 2023/03/21 15:19:29 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint
import os

def log(function):
	def wrapper(*args, **kwargs):
		func_name = function.__name__.replace('_', ' ').title()
		username = os.getenv('USER', "default_user")
		with open("machine.log", "a") as log_file:
			start = time.time()
			result = function(*args, **kwargs)
			exec_time = time.time() - start
			unit = 's'
			if exec_time < 0.001:
				unit = 'ms'
				exec_time *= 1000
			log_file.write(f'({username})Running: {func_name:19}[ exec-time = {exec_time:.3f} {unit} ]\n')
			return result
	return wrapper


class CoffeeMachine():
	
	water_level = 100
	
	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
		return False
	
	@log
	def boil_water(self):
		return "boiling..."
	
	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")
	
	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	machine.make_coffee()
	machine.add_water(70)