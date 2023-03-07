# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 04:58:46 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 03:26:49 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

def text_analyzer(text):
	"""
	This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.
	"""
	text = str(text)
	punctuation = str(string.punctuation)
	characters = len(text)
	upper_char = sum(1 for upper in text if upper.isupper())
	lower_char = sum(1 for lower in text if lower.islower())
	spaces = sum(1 for space in text if space.isspace())
	punctuation_char = sum(1 for punc in text if punctuation.find(punc) != -1)
	print("The text contains ", characters, "character(s):")
	print("- " , upper_char , " upper letter(s)")
	print("- " , lower_char , " lower letter(s)")
	print("- " , punctuation_char , " punctuation mark(s)")
	print("- " , spaces , " space(s)")

import sys

if __name__=="__main__":
	if len(sys.argv) > 2:
		print("Too much arguments.")
	elif len(sys.argv) < 2:
		user_input = input(">>>")
		text_analyzer(user_input)
	else :
		text_analyzer(sys.argv[1])