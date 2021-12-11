'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:
Input: nums = [1,2,3,4], k = 3
Output: false

Constraints:
1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
'''


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        #         if not nums or int(sum(nums)/k) != sum(nums)/k:
        #             return False

        #         def dfs(parts, nums, idx):
        #             if idx == len(nums):
        #                 return not sum(parts)
        #             for i in range(len(parts)):
        #                 if parts[i] >= nums[idx]:
        #                     parts[i] -= nums[idx]
        #                     if dfs(parts, nums, idx+1):
        #                         return True
        #                     parts[i] += nums[idx]

        #         nums.sort(reverse=True)
        #         parts = [sum(nums)/k]*k
        #         return dfs(parts, nums, 0)

        totalSum = sum(nums)
        if totalSum % k != 0: return False
        subSum = totalSum // k
        nums.sort(reverse=True)
        parts = [subSum] * k

        def findSubSum(parts, idx):
            if idx == len(nums): return not sum(parts)
            for i in range(len(parts)):
                if parts[i] >= nums[idx]:
                    parts[i] -= nums[idx]
                    if findSubSum(parts, idx + 1):
                        return True
                    parts[i] += nums[idx]
            return False

        return findSubSum(parts, 0)