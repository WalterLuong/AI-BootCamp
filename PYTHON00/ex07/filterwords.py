# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:10:15 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 04:17:08 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if len(sys.argv) != 3 or not sys.argv[2].isdigit():
	print("ERROR")
else:
	try:
		length = int(sys.argv[2])
	except ValueError as e:
		print("ERROR")
		exit(1)
	str_splitted = re.split("[][ !\"#$%&'()*+,-./:;<=>?@\^_`{|}~]" , sys.argv[1])
	ret_list = [word for word in str_splitted if len(word) > length]
	print(ret_list)