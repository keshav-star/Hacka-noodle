def swap(digits, i, j):
	digit = digits[i]
	digits[i] = digits[j]
	digits[j] = digit


# Find the minimum number formed by doing at-most `k` swap operations upon
# digits of the string
def findMin(digits, k, min_so_far):

	# compare the current number with a minimum number so far
	num = ''.join(digits)
	if num < min_so_far:
		min_so_far = num

	# base case: no swaps left
	if k < 1:
		return min_so_far

	# do for each digit in the input string
	for i in range(len(digits) - 1):

		# compare the current digit with the remaining digits
		for j in range(i + 1, len(digits)):

			# if the digit at i'th index is more than the digit at j'th index
			if digits[i] > digits[j]:
				# swap `digits[i]` with `digits[j]`
				swap(digits, i, j)

				# recur for remaining `k-1` swap
				min_so_far = findMin(digits, k - 1, min_so_far)

				# backtrack: restore the list
				swap(digits, i, j)

	return min_so_far


def findMinimum(s, k):

	# base case
	if not s:
		return s

	# convert digits of a given integer to a list of strings to
	# facilitate operations on them
	digits = list(s)
	return findMin(digits, k, s)


if __name__ == '__main__':

	# input number
	s = '934651'
	k = 2

	min = findMinimum(s, k)
	print(f'The minimum number formed by doing at-most {k} swaps is {min}')
