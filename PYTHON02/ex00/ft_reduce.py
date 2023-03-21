# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:19:19 by wluong            #+#    #+#              #
#    Updated: 2023/03/21 15:19:19 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, iterable):
	"""Apply function of two arguments cumulatively.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	A value, of same type of elements in the iterable parameter.
	None if the iterable can not be used by the function.
	"""
	if callable(function_to_apply) and hasattr(iterable, '__iter__') and len(iterable):
		val = iterable[0]
		for x in iterable[1::]:
			val = function_to_apply(val, x)
		return val
	else:
		return None

if __name__ == '__main__':
	lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
	# lst = [1, 2, 3]
	# lst = []
	print(ft_reduce(lambda u, v: u + v, lst))