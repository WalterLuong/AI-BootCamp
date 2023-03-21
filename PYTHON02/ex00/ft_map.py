# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:19:14 by wluong            #+#    #+#              #
#    Updated: 2023/03/21 15:19:15 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, iterable):
	"""Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	if callable(function_to_apply) and hasattr(iterable, '__iter__'):
		for x in iterable:
			yield function_to_apply(x)
	else:
		return None

if __name__ == '__main__':
	valid_list = [1, 2, 3, 4, 5]
	valid_tuple = (5, 9.4)

	print("\nFT_MAP TEST".ljust(50, "_"), end="\n\n")
	print(ft_map(lambda dum: dum + 1, valid_list))
	print(list(ft_map(lambda dum: dum + 1, valid_list)))
	print(ft_map(lambda dum: dum + 1, valid_tuple))
	print(tuple(ft_map(lambda dum: dum + 1, valid_tuple)))
	print("\nMAP TEST".ljust(50, "_"), end="\n\n")
	print(map(lambda dum: dum + 1, valid_list))
	print(list(map(lambda dum: dum + 1, valid_list)))
	print(map(lambda dum: dum + 1, valid_tuple))
	print(tuple(map(lambda dum: dum + 1, valid_tuple)))
