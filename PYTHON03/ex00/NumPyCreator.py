import numpy as np

class NumPyCreator:

	def __create_array(self, object, object_type):
		if not isinstance(object, object_type):
			return None
		if any(isinstance(x, object_type) for x in object) and not all(isinstance(x, object_type) for x in object):
			return None
		if any(isinstance(x, object_type) for x in object):
			length = len(object[0])
			if not all(len(lst) == length for lst in object):
				return None
		return np.array(object)

	def __check_shape(self, shape):
		if not isinstance(shape, tuple):
			return False
		if not all(isinstance(x, int) for x in shape):
			return False
		if any(x < 0 for x in shape):
			return False
		return True

	def from_list(self, lst):
		return self.__create_array(lst, list)

	def from_tuple(self, tpl):
		return self.__create_array(tpl, tuple)

	def from_iterable(self, itr):
		if not hasattr(itr, '__iter__'):
			return None
		return self.from_list(list(itr))

	def from_shape(self, shape, value=0):
		if not self.__check_shape(shape):
			return None
		return np.full(shape, value)

	def random(self, shape):
		if not self.__check_shape(shape):
			return None
		return np.random.random(shape)
	
	def identity(self, n):
		if not isinstance(n, int) or n < 0:
			return None
		return np.identity(n)


if __name__ == '__main__':
	npc = NumPyCreator()
	list_a = [1, 2, 3, 4]
	list_b = [5,6,7,8]
	a = npc.from_list([[1,2,3],[6,3,4]])
	print(a)
	b = npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])
	print(b)
	c = npc.from_iterable(range(5))
	print(c)
	d = npc.identity(-5)
	print(d)
	shape = (3,5)
	e = npc.from_shape(shape, 1)
	print(e)
	f = npc.random(shape)
	print(f)