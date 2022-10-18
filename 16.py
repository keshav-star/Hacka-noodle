# Function to determine whether a string matches with a given pattern
def isMatch(word, pattern, d, i=0, j=0):

	# invalid input
	if not word or not pattern:
		return False

	n = len(word)
	m = len(pattern)

	# base condition
	if n < m:
		return False

	# if both pattern and the string reaches the end
	if i == n and j == m:
		return True

	# if either string or pattern reaches the end
	if i == n or j == m:
		return False

	# consider the next character from the pattern
	curr = pattern[j]

	# if the character is seen before
	if curr in d:

		s = d[curr]
		k = len(s)

		# `ss` stores next `k` characters of the given string
		if i + k < len(word):
			ss = word[i:i + k]
		else:
			ss = word[i:]

		# return false if the next `k` characters don't match with `s`
		if ss != s:
			return False

		# recur for remaining characters if the next `k` characters match
		return isMatch(word, pattern, d, i + k, j + 1)

	# process all remaining characters in the string if the current
	# character is never seen before
	for k in range(1, n - i + 1):

		# insert substring formed by next `k` characters of the string
		# into the dictionary
		d[curr] = word[i:i + k]

		# check if it leads to the solution
		if isMatch(word, pattern, d, i + k, j + 1):
			return True

		# otherwise, backtrack – remove the current character from the dictionary
		d.pop(curr)

	return False


if __name__ == '__main__':

	# input string and pattern
	word = 'codesleepcode'
	pattern = 'XYX'

	# create a dictionary to store mappings between the pattern and string
	d = {}

	# check for solution
	if isMatch(word, pattern, d):
		print(d)
	else:
		print('Solution doesn\'t exist')
