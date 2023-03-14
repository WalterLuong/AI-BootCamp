from vector import Vector
import sys

if __name__ == '__main__':
	sys.tracebacklimit = 0
	print("Subject test".ljust(42, '_'))
	# Column vector of shape (n, 1)
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
	# Expected output
	# (4,1)
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
	# Expected output
	# [[0.0], [1.0], [2.0], [3.0]]
	# Row vector of shape (1, n)
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
	# Expected output
	# (1,4)
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
	# Expected output
	# [[0.0, 1.0, 2.0, 3.0]]
	print("Example 1 ".ljust(42, '_'))
	v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	print(v1.shape)
	# Expected output:
	# (4,1)
	print(v1.T())
	# Expected output:
	# Vector([[0.0, 1.0, 2.0, 3.0]])
	print(v1.T().shape)
	# Expected output:
	# (1,4)
	print("Example 2 ".ljust(42, '_'))
	v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
	print(v2.shape)
	# Expected output:
	# (1,4)
	print(v2.T())
	# Expected output:
	# Vector([[0.0], [1.0], [2.0], [3.0]])
	print(v2.T().shape)
	# Expected output:
	# (4,1)

	print("Dot function ".ljust(42, '_'))
	# Example 1:
	v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
	print(v1.dot(v2))
	# Expected output:
	# 18.0
	v3 = Vector([[1.0], [3.0]])
	v4 = Vector([[2.0], [4.0]])
	print(v3.dot(v4))
	# Expected output:
	# 13.0
	v1
	print(v1)
	# Expected output: to see what __str__() should do
	# [[0.0, 1.0, 2.0, 3.0]]
	print("Test de calculs ".ljust(42, '_'))
	wawa = v4 + v3
	wawa2 = v4 - v3 - v4
	print(wawa)
	print(wawa2)
	print(2 * wawa * 0)
	print(v4 * 3 / 2)
	print(2 / wawa)