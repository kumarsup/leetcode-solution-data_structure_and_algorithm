'''
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.



Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.


Constraints:

1 <= nums.length <= 2 * 105
-104 <= nums[i] <= 104
-109 <= k <= 109
'''
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        currSum, lookup = nums[0], {}
        maxLength = 1 if currSum==k else 0
        lookup[currSum]= 0
        for i in range(1, len(nums)):
            currSum = currSum + nums[i]
            if currSum not in lookup: lookup[currSum] = i
            if currSum == k: maxLength = max(maxLength, i+1)
            if currSum-k in lookup: maxLength = max(maxLength, i-lookup[currSum-k])
        return maxLength