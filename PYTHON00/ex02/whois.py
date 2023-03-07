# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 04:28:33 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 04:28:34 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

number = 0

if len(sys.argv) > 2:
	print("AssertionError: more than one argument are provided")
elif len(sys.argv) < 2:
	print("AssertionError: you should have an argument")
else:
	try:
		number = int(sys.argv[-1])
	except ValueError as e:
		print("AssertionError: argument is not an integer")
		exit(1)
	if (number == 0) :
		print("I'm Zero.")
	elif number % 2 == 0 :
		print("I'm Even.")
	else:
		print("I'm Odd.")