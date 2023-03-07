# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:10:07 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 03:36:15 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def print_sum(a, b):
	"""
	Renvoie la somme de a + b
	"""
	print("\033[1;31mSum:\033[m\t\t%d" % (a + b))

def print_difference(a, b):
	"""
	Renvoie la difference de a - b
	"""
	print("\033[1;32mDifference:\033[m\t%d" % (a - b))

def print_product(a, b):
	"""
	Renvoie le produit de a x b
	"""
	print("\033[1;33mProduct:\033[m\t%d" % (a * b))

def print_quotient(a, b):
	"""
	Renvoie le quotient de a / b
	"""
	if b == 0:
		print("\033[1;34mQuotient:\033[m\tERROR (division by zero)")
	else:
		print("\033[1;34mQuotient:\033[m\t%.3f" % (a / b))

def print_remainder(a, b):
	"""
	Renvoie le modulo de a % b
	"""
	if b == 0:
		print("\033[1;35mRemainder:\033[m\tERROR (modulo by zero)")
	else:
		print("\033[1;35mRemainder:\033[m\t%d" % (a % b))

import sys

if __name__=="__main__":
	if len(sys.argv) != 3 :
		print("AssertionError: You must have 2 numeric arguments.")
	else:

		for args in sys.argv[1::]:
			try:
				int(args)
			except ValueError as e:
				print("AssertionError: only integers")
				exit(1)
		print_sum(int(sys.argv[1]), int(sys.argv[2]))
		print_difference(int(sys.argv[1]), int(sys.argv[2]))
		print_product(int(sys.argv[1]), int(sys.argv[2]))
		print_quotient(int(sys.argv[1]), int(sys.argv[2]))
		print_remainder(int(sys.argv[1]), int(sys.argv[2]))