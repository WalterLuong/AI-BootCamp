import csv

class CsvReader():

	def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.filename = filename
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom

	def __enter__(self):
		self.dataset = []
		if hasattr(self, 'filename'):
			self.csv = open(self.filename, 'r')
			for line in self.csv:
				print(list(map(str.strip, line.split(self.sep))))
			return self
		else:
			return None

	def __exit__(self):
		if hasattr(self, 'filename'):
			self.csv.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom.
		Return:
		nested list (list(list, list, ...)) representing the data.
		"""
		pass

	def getheader(self):
		""" Retrieves the header from csv file.
		Returns:
		list: representing the data (when self.header is True).
		None: (when self.header is False).
		"""
		pass