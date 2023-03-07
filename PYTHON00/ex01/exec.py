# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/07 04:28:28 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 04:28:30 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

arguments = ""
final_string = ""

for strings in sys.argv[1::]:
	arguments += strings
	if strings != sys.argv[-1] :
		arguments += " "


for letter in arguments[::-1]:
	if (letter.isupper()):
		final_string += letter.lower()
	elif (letter.islower()):
		final_string += letter.upper()
	else:
		final_string += letter


print(final_string)