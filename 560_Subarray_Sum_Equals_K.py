'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache, sumA, count = defaultdict(int), 0, 0
        cache[0] = 1
        for i in range(len(nums)):
            sumA += nums[i]
            if sumA-k in cache: count += cache[sumA-k]
            if sumA in cache: cache[sumA] += 1
            else: cache[sumA] = 1
        return count