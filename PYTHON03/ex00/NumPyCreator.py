import numpy as np

class NumPyCreator:


	def from_list(self, lst):
		return np.array(lst)

	def from_tuple(self, tpl):
		return np.asarray(tpl)
	
	def identity(self, n):
		if not isinstance(n, int):
			print("The parameter n must be an int.")
			return None
		return np.identity(n)


if __name__ == '__main__':
	npc = NumPyCreator()
	list_a = [1, 2, 3, 4]
	list_b = [5,6,7,8]
	a = npc.from_tuple(["a", "b", "c"])
	print(a)