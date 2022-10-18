# Recursive function to get all routes in a rectangular grid
# that start at cell (i, j) and ends at the last cell (M-1, N-1).
def printPaths(mat, route=[], i=0, j=0):

	# base case
	if not mat or not len(mat):
		return

	# `M × N` matrix
	(M, N) = (len(mat), len(mat[0]))

	# include current cell in route
	route.append(mat[i][j])

	# if the last cell is reached
	if i == M - 1 and j == N - 1:
		print(route)
	else:
		# move down
		if i + 1 < M:
			printPaths(mat, route, i + 1, j)

		# move right
		if j + 1 < N:
			printPaths(mat, route, i, j + 1)

		# move diagonally
		if i + 1 < M and j + 1 < N:
			printPaths(mat, route, i + 1, j + 1)

	# backtrack: remove the current cell from the route
	route.pop()


if __name__ == '__main__':

	mat = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]

	printPaths(mat)
