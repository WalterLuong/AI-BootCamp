# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:19:12 by wluong            #+#    #+#              #
#    Updated: 2023/03/21 15:19:13 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None
	"""
	if callable(function_to_apply) and hasattr(iterable, '__iter__'):
		for x in iterable:
			if function_to_apply(x):
				yield x
	else:
		return None

if __name__ == '__main__':
	valid_list = [1, 2, 3, 4, 5]
	valid_tuple = (5, 9.4, 4)

	print("\nFT_FILTER TEST".ljust(50, "_"), end="\n\n")
	print(ft_filter(lambda dum: not (dum % 2), valid_list))
	print(list(ft_filter(lambda dum: not (dum % 2), valid_list)))
	print(ft_filter(lambda dum: not (dum % 2), valid_tuple))
	print(tuple(ft_filter(lambda dum: not (dum % 2), valid_tuple)))
	print("\nFILTER TEST".ljust(50, "_"), end="\n\n")
	print(filter(lambda dum: not (dum % 2), valid_list))
	print(list(filter(lambda dum: not (dum % 2), valid_list)))
	print(filter(lambda dum: not (dum % 2), valid_tuple))
	print(tuple(filter(lambda dum: not (dum % 2), valid_tuple)))