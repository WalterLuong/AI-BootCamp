from csvreader import CsvReader

with CsvReader('good.csv', ',', True) as file:
	if file == None:
		print("File is corrupted")
	else:
		data = file.getdata()
		header = file.getheader()
		print("Data = " + str(data), end='\n\n')
		print("Header = " + str(header))