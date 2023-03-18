import numpy as np

class NumPyCreator:

	def from_list(self, lst, datatype=None):
		return np.array(lst, datatype)
	
	def identity(self, n):
		if not isinstance(n, int):
			print("The parameter n must be an int.")
			return None
		return np.identity(n)