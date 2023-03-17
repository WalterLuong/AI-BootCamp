import numpy as np

class NumPyCreator:

	def from_list(self, lst, datatype=None):
		return np.array(lst, datatype)