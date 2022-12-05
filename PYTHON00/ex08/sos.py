# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:10:20 by wluong            #+#    #+#              #
#    Updated: 2022/12/05 05:11:03 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ' ' : '/'}

def encript(msg):
	encripted_message = ''
	msg = msg.upper()
	for letter in msg:
		if not letter == msg[-1]:
			encripted_message += morse[letter] + ' '
		else:
			encripted_message += morse[letter]
	return encripted_message

for arg in sys.argv[1::]:
	for letter in arg:
		if not letter.isalnum() and not letter.isspace():
			print("ERROR")
			break
	else:
		print(encript(arg), end = '')
		if not arg == sys.argv[-1]:
			print(" / ", end="")
