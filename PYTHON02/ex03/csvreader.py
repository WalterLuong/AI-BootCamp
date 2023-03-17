class CsvReader():

	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		self.dataset = []
		if hasattr(self, 'filename') and self.filename:
			self.csv = open(self.filename, 'r')
			for line in self.csv:
				self.dataset.append(list((x.strip(' "\n') for x in line.split(self.sep))))
			for cell in self.dataset:
				if len(cell) != len(self.dataset[0]):
					return None
				for case in cell:
					if len(case) == 0:
						return None
			return self
		else:
			self.csv = None
			return self.csv

	def __exit__(self, exception_type, exception_value, exception_traceback):
		if hasattr(self, 'filename') and self.csv:
			self.csv.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		start = self.skip_top
		if self.header:
			start += 1
		return self.dataset[start:len(self.dataset) - self.skip_bottom]

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		if self.header:
			return self.dataset[0]
		return None