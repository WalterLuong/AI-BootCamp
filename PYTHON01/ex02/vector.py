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
		if isinstance(values, list):
			if is_row(values):
				self.values = values
				self.shape = (1, len(values[0]))
			elif is_column(values):
				self.values = values
				self.shape = (len(values), 1)
			else:
				raise ValueError("\033[1;31mBad parameters for the vector's creation\033[m")
		elif isinstance(values, (int, tuple)):
			if is_size(values):
				self.values = []
				for x in range(values):
					self.values.append([float(x)])
				self.shape = (values, 1)
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
		else:
			raise ValueError("\033[1;31mBad parameters for the vector's creation\033[m")
		
	def __str__(self) -> str:
		"""Show the attributes of the vector"""
		return str(self.values)

	def __repr__(self) -> str:
		return str(self.values)

	def __add__(self, other):
		if isinstance(other, Vector):
			if self.shape == other.shape:
				if is_column(self.values):
					result = []
					for i in range(len(self.values)):
						result.append([self.values[i][0] + other.values[i][0]])
					return Vector(result)
				else:
					return Vector([[sum(x) for x in zip(self.values[0], other.values[0])]])
			else:
				raise ValueError("Vectors must have the same shape.")
		else:
			ValueError("The addition is only between 2 vectors.")

	def __radd__(self, other):
		return self.__add__(other)
	
	def __mul__(self, scalar):
		if isinstance(scalar, (int, float)):
			if is_row(self.values):
				return Vector([[x * scalar for x in self.values[0]]])
			else:
				result = []
				for i in range(len(self.values)):
					result.append([self.values[i][0] * scalar])
				return Vector(result)
		else:
			raise ValueError("You only can multiply a vector by a scalar.")
			
	def __rmul__(self, scalar):
		return self.__mul__(scalar)
	
	def __sub__(self, other):
		return self.__add__(other * -1)
	
	def __rsub__(self, other):
		return self.__sub__(other)
	
	def __truediv__(self, scalar):
		return self.__mul__(1/scalar)
	
	def __rtruediv__(self, scalar):
		raise NotImplementedError("Division of a scalar by a Vector is not defined here.")


	def T(self):
		T = []
		if is_column(self.values):
			row = []
			for elem in self.values:
				row.append(elem[0])
			T.append(row)
			return Vector(T)
		else:
			for elem in self.values[0]:
				T.append([elem])
			return Vector(T)

	def dot(self, v):
		if not isinstance(v, Vector):
			raise ValueError("Dot product must be between 2 vectors")
		if self.shape != v.shape:
			raise ValueError("Vectors must have the same shape to apply the dot product")
		else:
			if is_column(self.values):
				result = sum(self.values[i][0] * v.values[i][0] for i in range(len(self.values)))
				return result
			else:
				result = sum(self.values[0][i] * v.values[0][i] for i in range(len(self.values[0])))
				return result