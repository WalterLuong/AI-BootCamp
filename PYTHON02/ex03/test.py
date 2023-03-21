# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:19:36 by wluong            #+#    #+#              #
#    Updated: 2023/03/21 15:19:36 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from csvreader import CsvReader

with CsvReader('godod.csv', ',', True) as file:
	if file == None:
		print("File is corrupted")
	else:
		data = file.getdata()
		header = file.getheader()
		print("Data = " + str(data), end='\n\n')
		print("Header = " + str(header))