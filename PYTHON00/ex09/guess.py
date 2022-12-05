# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:11:11 by wluong            #+#    #+#              #
#    Updated: 2022/12/05 05:11:12 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

magic_number = random.randint(1, 99)
# magic_number = 42
attempts = 0
while True:
	print("\033[1;33mWhat's your guess between 1 and 99 ?\033[m")
	response = input(">>> ")
	if not response.isdigit() and response != "exit":
		print("\033[1;31mThat's not a number.\n\033[m")
	else:
		attempts += 1
		if response == "exit":
			print("\n\033[1;32mGoodbye\033[m")
			break
		elif int(response) < magic_number:
			print("\033[36mToo low !\n\033[m")
		elif int(response) > magic_number:
			print("\033[35mToo high\n\033m")
		elif int(response) == magic_number:
			if magic_number == 42:
				print("\033[32mThe answer to the ultimate question of life, the universe and everything is 42\033[m")
			if attempts == 1:
				print("\033[32mCongratulations! You got it on your first try!\033[m")
				break
			else:
				print("\033[32mCongratulations, you've got it!\nYou won in %d attempts!\033[m" %attempts)
				break


