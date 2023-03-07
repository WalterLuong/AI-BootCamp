# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: wluong <wluong@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/12/05 05:11:30 by wluong            #+#    #+#              #
#    Updated: 2022/12/07 04:27:21 by wluong           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import sys

def ft_progress(lst):
	start_time = time.time()
	bar_size = 30
	for i in range(len(lst)):
		ratio = (i + 1) * 100 / len(lst)
		elapsed_time = time.time() - start_time
		eta = elapsed_time / ratio * 100 - elapsed_time 
		bar = ("█" * int(ratio / 100 * bar_size))
		if ratio != 100:
			color = "\033[1;31m"
		else:
			color = "\033[1;32m"
		datas = (eta, color, ratio, color, bar.ljust(bar_size, ' '), i + 1, len(lst),elapsed_time)
		print("\rETA: %.2fs [%s%3d%%\033[m] [%s%s\033[m] %d/%d | elapsed time %.2fs" % datas, end="")
		yield i


if __name__ == "__main__":
	listy = range(-1, 1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		time.sleep(0.005)
	print()
	print(ret)