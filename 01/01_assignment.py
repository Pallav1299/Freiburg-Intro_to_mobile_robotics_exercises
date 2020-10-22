import numpy as np

"""
1. check if square
2. Check if diagonal elements are 1 and non-diagonal elements are 0  ## NOT REQUIRED
3. A*A.T = I
"""

def matrix_orthogonality_check(mat):
	# check 1
	if (mat.shape[0] != mat.shape[1]):	
		return 0

	# check 2   ## NOT REQUIRED
	# for i in range(0, mat.shape[0]-1):
	# 	for j in range(0, mat.shape[1]-1):
	# 		if i==j and mat[i][j] != 1:
	# 			return 0
	# 		elif mat[i][j] != 0:
	# 			return 0

	# check 3
	A = np.dot(mat, mat.T)
	if (np.array_equal(A,np.identity(mat.shape[0]))):
		return 0
	else:
		return 1


def main():
	D = 1./3. * np.array([[2, 2, -1],
						[2, -1, 2],
						[-1, 2, 2]])
	print(matrix_orthogonality_check(D))

if __name__=="__main__":
	main()