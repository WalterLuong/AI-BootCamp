def what_are_the_vars(*args, **kwargs):
	"""
	...
	"""
	object = ObjectC()
	for key, value in kwargs.items():
		setattr(object, key, value)
	for key, value in enumerate(args):
		val_i = "var_{}".format(key)
		setattr(object, val_i, value)
	return object

class ObjectC(object):

	def __init__(self) -> None:
		pass

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = None
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", a=10, var_2="world")
	doom_printer(obj)

