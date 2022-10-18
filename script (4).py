# To store cell coordinates of the matrix
class Node:
	def __init__(self, first, second):
		self.first = first
		self.second = second


# Below lists detail all four possible movements from a cell
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]


# Function to check if it is possible to go to position `pt`
# from the current position. The function returns false if `pt` is
# not a valid position, or it is already visited
def isValid(path, pt, N):
	return 0 <= pt.first < N and 0 <= pt.second < N and \
		not any(x for x in path if x.first == pt.first and x.second == pt.second)


# Function to print the complete path from source to destination
def printPath(path):
	for cell in path:
		print((cell.first, cell.second), end=' ')


# Find a route in a matrix `mat` from source cell (0, 0) to
# destination cell (N-1, N-1)
def findPath(mat, path, curr):

	# base case
	if not mat or not len(mat):
		return 0

	# include current vertex in the path
	path.append(curr)

	# `N × N` matrix
	N = len(mat)

	# if the destination is found, return true
	if curr.first == N - 1 and curr.second == N - 1:
		return True

	# get the value of the current cell
	n = mat[curr.first][curr.second]

	# check all four possible movements from the current cell
	# and recur for each valid movement
	for i in range(len(row)):

		# get the next position using the value of the current cell
		x = curr.first + row[i] * n
		y = curr.second + col[i] * n

		next = Node(x, y)

		# check if it is possible to go to a position (x, y)
		# from the current position
		if isValid(path, next, N) and findPath(mat, path, next):
			return True

	# backtrack: exclude the current cell from the path
	path.pop()
	return False


if __name__ == '__main__':

	mat = [
		[7, 1, 3, 5, 3, 6, 1, 1, 7, 5],
		[2, 3, 6, 1, 1, 6, 6, 6, 1, 2],
		[6, 1, 7, 2, 1, 4, 7, 6, 6, 2],
		[6, 6, 7, 1, 3, 3, 5, 1, 3, 4],
		[5, 5, 6, 1, 5, 4, 6, 1, 7, 4],
		[3, 5, 5, 2, 7, 5, 3, 4, 3, 6],
		[4, 1, 4, 3, 6, 4, 5, 3, 2, 6],
		[4, 4, 1, 7, 4, 3, 3, 1, 4, 2],
		[4, 4, 5, 1, 5, 2, 3, 5, 3, 5],
		[3, 6, 3, 5, 2, 2, 6, 4, 2, 1]
	]

	path = []
	source = Node(0, 0)

	# Find a route in a matrix `mat` from source cell (0, 0) to
	# destination cell (N-1, N-1)
	if findPath(mat, path, source):
		printPath(path)
