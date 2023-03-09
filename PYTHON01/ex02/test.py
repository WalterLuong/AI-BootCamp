from vector import Vector
import sys

if __name__ == '__main__':
	sys.tracebacklimit = 0
	v1 = Vector([[1, 2, 3]])
	print(v1.values)
	print(v1.shape)

	v2 = Vector([[3.], [4.], [5.]])
	print(v2.values)
	print(v2.shape)
	print(v2)
	v2.T()
	print(v2)
	v3 = Vector([[4, 5, 6, 7]])
	print(v3)
	v3.T()
	print(v3)