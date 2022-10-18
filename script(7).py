# Check if cell (x, y) is valid or not
def isValidCell(x, y, N):
	return not (x < 0 or y < 0 or x >= N or y >= N)


def countPaths(maze, i, j, dest, visited):

	# `N × N` matrix
	N = len(maze)

	# if destination (x, y) is found, return 1
	if (i, j) == dest:
		return 1

	# stores number of unique paths from source to destination
	count = 0

	# mark the current cell as visited
	visited[i][j] = True

	# if the current cell is a valid and open cell
	if isValidCell(i, j, N) and maze[i][j] == 1:

		# go down (i, j) ——> (i + 1, j)
		if i + 1 < N and not visited[i + 1][j]:
			count += countPaths(maze, i + 1, j, dest, visited)

		# go up (i, j) ——> (i - 1, j)
		if i - 1 >= 0 and not visited[i - 1][j]:
			count += countPaths(maze, i - 1, j, dest, visited)

		# go right (i, j) ——> (i, j + 1)
		if j + 1 < N and not visited[i][j + 1]:
			count += countPaths(maze, i, j + 1, dest, visited)

		# go left (i, j) ——> (i, j - 1)
		if j - 1 >= 0 and not visited[i][j - 1]:
			count += countPaths(maze, i, j - 1, dest, visited)

	# backtrack from the current cell and remove it from the current path
	visited[i][j] = False

	return count


def findCount(maze, src, dest):

	# get source cell (i, j)
	i, j = src

	# get destination cell (x, y)
	x, y = dest

	# base case: invalid input
	if not maze or not len(maze) or not maze[i][j] or not maze[x][y]:
		return 0

	# `N × N` matrix
	N = len(maze)

	# 2D matrix to keep track of cells involved in the current path
	visited = [[False for x in range(N)] for y in range(N)]

	# start from source cell (i, j)
	return countPaths(maze, i, j, dest, visited)


if __name__ == '__main__':

	maze = [
		[1, 1, 1, 1],
		[1, 1, 0, 1],
		[0, 1, 0, 1],
		[1, 1, 1, 1]
	]

	# source cell
	src = (0, 0)

	# destination cell
	dest = (3, 3)

	print("The total number of unique paths are", findCount(maze, src, dest))
