class Solution:
	def twoSum(self, nums: list[int], target: int)-> List[int]:
		n = len(nums)
		sumMap = collections.defaultdict(int)
		for i in range(n):
			value = nums[i]
			if target - value in sumMap:
				return [sumMap[target - value], i]
			else:
				sumMap[value] = i
		return [-1, -1]
