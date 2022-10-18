# Find all binary strings that can be formed from a given wildcard pattern
def printAllCombinations(pattern, i=0):

	# base case
	if not pattern:
		return

	if i == len(pattern):
		print(''.join(pattern))
		return

	# if the current character is '?'
	if pattern[i] == '?':
		for ch in '01':

			# replace '?' with 0 and 1
			pattern[i] = ch

			# recur for the remaining pattern
			printAllCombinations(pattern, i + 1)

			# backtrack
			pattern[i] = '?'

	else:
		# if the current character is 0 or 1, ignore it and
		# recur for the remaining pattern
		printAllCombinations(pattern, i + 1)


if __name__ == '__main__':

	pattern = '1?11?00?1?'
	printAllCombinations(list(pattern))
