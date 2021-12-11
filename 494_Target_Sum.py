'''
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''
import numpy as np


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [[None] * 2001 for _ in range(N)]

        def recursive(sumA=0, idx=0):
            nonlocal dp
            if idx > len(nums): return 0
            if idx == len(nums):
                if sumA == target:
                    return 1
                else:
                    return 0
            if dp[idx][sumA + 1000] is not None: return dp[idx][sumA + 1000]

            res1 = recursive(sumA - nums[idx], idx + 1)
            res2 = recursive(sumA + nums[idx], idx + 1)
            dp[idx][sumA + 1000] = res1 + res2
            return dp[idx][sumA + 1000]

        return recursive()