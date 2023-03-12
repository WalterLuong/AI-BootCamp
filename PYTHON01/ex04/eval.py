class Evaluator:
	@staticmethod
	def zip_evaluate(coefs, words):
		if isinstance(words, list) and isinstance(coefs, list):
			if all(isinstance(x, str) for x in words) and all(isinstance(y, (int, float)) for y in coefs):
				if len(words) == len(coefs):
					total_lenght = 0
					zipped = zip(words, coefs)
					for x in zipped:
						total_lenght += len(x[0]) * x[1]
					return total_lenght
				return -1
			raise ValueError("Words must be a list of strings and coefs must be a list of int/float")
		raise ValueError("Words and Coefs must be lists")
	
	@staticmethod
	def enumerate_evaluate(coefs, words):
		if isinstance(words, list) and isinstance(coefs, list):
			if all(isinstance(x, str) for x in words) and all(isinstance(y, (int, float)) for y in coefs):
				if len(words) == len(coefs):
					total_lenght = 0
					for count, value in enumerate(words):
						total_lenght += coefs[count] * len(value)
					return total_lenght
				return -1
			raise ValueError("Words must be a list of strings and coefs must be a list of int/float")
		raise ValueError("Words and Coefs must be lists")

if __name__ == '__main__':
	words = ["Le", "Lorem", "Ipsum", "est", "simple"]
	coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))
	words = ["salut", "les", "amis"]
	coefs = [1.0, 2.0, 3.0]
	print(Evaluator.zip_evaluate(coefs, words))
	print(Evaluator.enumerate_evaluate(coefs, words))