import array as arr

class TinyStatistician():

	@staticmethod
	def mean(x) -> float:
		if isinstance(x, list):
			if all(isinstance(i, (float, int)) for i in x):
				if len(x) == 0:
					return None
				else:
					return sum(x) / len(x)
			return None
		return None

	@staticmethod
	def median(x) -> float:
		if isinstance(x, list):
			if all(isinstance(i, (float, int)) for i in x):
				if len(x) == 0:
					return None
				tmp = x
				tmp.sort()
				return float(tmp[int(len(x) / 2)])
			return None
		return None

	@staticmethod
	def quartiles(x) -> list:
		if isinstance(x, list):
			if all(isinstance(i, (float, int)) for i in x):
				if len(x) == 0:
					return None
				tmp = x
				tmp.sort()
				quartiles = []
				quartiles.append(float(tmp[int(0.25*len(tmp))]))
				quartiles.append(float(tmp[int(0.75*len(tmp))]))
				return quartiles
			return None
		return None

	@staticmethod
	def var(x) -> float:
		if isinstance(x, list):
			if all(isinstance(i, (float, int)) for i in x):
				if len(x) == 0:
					return None
				var = 0
				for i in x:
					var += (i - TinyStatistician.mean(x)) ** 2
				return float(var) / len(x)
			return None
		return None

	@staticmethod
	def std(x):
		if isinstance(x, list):
			if all(isinstance(i, (float, int)) for i in x):
				if len(x) == 0:
					return None
				return TinyStatistician.var(x) ** 0.5
			return None
		return None


if __name__ == '__main__':
	
	tstat = TinyStatistician()
	a = [1, 42, 300, 10, 59]
	print(tstat.mean(a))
	print(tstat.median(a))
	print(tstat.quartiles(a))
	print(tstat.var(a))
	print(tstat.std(a))