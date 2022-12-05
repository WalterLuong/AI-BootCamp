# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:10:07 by wluong            #+#    #+#              #
#    Updated: 2022/12/05 05:10:08 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def sum(a, b):
	"""
	Renvoie la somme de a + b
	"""
	print("\033[1;31mSum:\033[m\t\t%d" % (a + b))

def difference(a, b):
	"""
	Renvoie la difference de a - b
	"""
	print("\033[1;32mDifference:\033[m\t%d" % (a - b))

def product(a, b):
	"""
	Renvoie le produit de a x b
	"""
	print("\033[1;33mProduct:\033[m\t%d" % (a * b))

def quotient(a, b):
	"""
	Renvoie le quotient de a / b
	"""
	if b == 0:
		print("\033[1;34mQuotient:\033[m\tERROR (division by zero)")
	else:
		print("\033[1;34mQuotient:\033[m\t%.3f" % (a / b))

def reminder(a, b):
	"""
	Renvoie le modulo de a % b
	"""
	if b == 0:
		print("\033[1;35mReminder:\033[m\tERROR (modulo by zero)")
	else:
		print("\033[1;35mReminder:\033[m\t%d" % (a % b))

import sys

if __name__=="__main__":
	if len(sys.argv) != 3 :
		print("AssertionError: You must have 2 numeric arguments.")
	else:
		error = 0
		for args in sys.argv[1::]:
			if not args.isdigit() and not args[0] == "-":
				print("AssertionError: only integers.")
				error = 1
				break
		if error == 0:
			sum(int(sys.argv[1]), int(sys.argv[2]))
			difference(int(sys.argv[1]), int(sys.argv[2]))
			product(int(sys.argv[1]), int(sys.argv[2]))
			quotient(int(sys.argv[1]), int(sys.argv[2]))
			reminder(int(sys.argv[1]), int(sys.argv[2]))