# Count ways to calculate a target from elements of a specified list
def countWays(nums, n, target):

	# base case: if a target is found
	if target == 0:
		return 1

	# base case: no elements are left
	if n < 0:
		return 0

	# 1. ignore the current element
	exclude = countWays(nums, n - 1, target)

	# 2. Consider the current element
	#	2.1. Subtract the current element from the target
	#	2.2. Add the current element to the target
	include = countWays(nums, n - 1, target - nums[n]) + countWays(nums, n - 1, target + nums[n])

	# Return total count
	return exclude + include


if __name__ == '__main__':

	# input list and target number
	nums = [5, 3, -6, 2]
	target = 6

	print(countWays(nums, len(nums) - 1, target), 'ways')
