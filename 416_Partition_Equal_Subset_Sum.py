'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets
such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum, N = sum(nums), len(nums)
        if totalSum % 2 != 0: return False
        subSum = totalSum // 2

        dp = [[None] * (subSum + 1) for _ in range(N + 1)]
        dp[0][0] = True

        for i in range(1, N + 1):
            curr = nums[i - 1]
            for j in range(subSum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[N][subSum]