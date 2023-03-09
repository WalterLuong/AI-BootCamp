def is_column(values) -> bool:
	"""Check if the vector is a column (dimension [n, 1])"""
	if all(isinstance(x, list) for x in values):
		for x in values:
			if not all(isinstance(n, (int, float)) for n in x) or len(x) != 1:
				return False
		return True
	return False

def is_row(values) -> bool :
	"""Check if the vector is a row (dimension [1, n])"""
	if all(isinstance(x, list) for x in values) and len(values) == 1:
		for x in values:
			if not all(isinstance(n, (int, float)) for n in x):
				return False
		return True
	return False

def is_size(values) -> bool :
	"""Check if the vector is initialized by a size"""
	if isinstance(values, int):
		return True
	return False

def is_range(values) -> bool:
	"""Check if the vector is initialized by a range"""
	if isinstance(values, tuple) and len(values) == 2:
		if all(isinstance(x, int) for x in values):
			return True
	return False

class Vector:
	"""A vector class which can be used for maths operations"""
	def __init__(self, values) -> None:
		"""Initialization of the Vector"""
		if is_size(values):
			self.values = []
			for x in range(values):
				self.values.append([float(x)])
			self.shape = (values, 1)
		elif is_row(values):
			self.values = values
			self.shape = (1, len(values[0]))
		elif is_column(values):
			self.values = values
			self.shape = (len(values), 1)
		elif is_range(values):
			if values[0] > values[1]:
				raise ValueError("Can't initialize a Vector with a range (a, b) where a > b")
			else:
				self.values = []
				for x in range(values[0], values[1]):
					self.values.append([float(x)])
				self.shape = (values[1] - values[0], 1)
		else:
			raise ValueError("\033[1;31mBad parameters for the vector's creation\033[m")
		
	def __str__(self) -> str:
		"""Show the attributes of the vector"""
		text = ("Values: " + str(self.values) + '\n'
		+ 'Shape: ' + str(self.shape))
		return text

	def T(self):
		T = []
		if is_column(self.values):
			row = []
			for elem in self.values:
				row.append(elem[0])
			T.append(row)
			self.values = T
			self.shape = self.shape[::-1]
		else:
			for elem in self.values[0]:
				T.append([elem])
			self.values = T
			self.shape = self.shape[::-1]
	# def dot(self, v):
	# 	if not isinstance(v, Vector):
	# 		raise ValueError("Dot product must be between 2 vectors")
	# 	Tshape = v.shape[::-1]
	# 	if self.shape != v.shape and self.shape != Tshape:
	# 		raise ValueError("Vectors must have the same shape to apply the dot product")
	# 	else:
