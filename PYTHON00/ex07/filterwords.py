# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:10:15 by wluong            #+#    #+#              #
#    Updated: 2022/12/05 05:10:15 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if len(sys.argv) != 3 or not sys.argv[2].isdigit():
	print("ERROR")
else:
	str_splitted = re.split("[][ !\"#$%&'()*+,-./:;<=>?@\^_`{|}~]" , sys.argv[1])
	ret_list = [word for word in str_splitted if len(word) > int(sys.argv[2])]
	print(ret_list)