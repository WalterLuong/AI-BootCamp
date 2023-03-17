import time
from my_minipack.progress import ft_progress

if __name__ == "__main__":
	listy = range(-1, 1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += elem
		time.sleep(0.005)
	print()
	print(ret)