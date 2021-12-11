'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        N, maxLength = len(nums), 1
        dp = [1] * N

        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = 1 + dp[j]
                    maxLength = max(maxLength, dp[i])
        return maxLength

#         N = len(nums)
#         dp = [[None]*N for _ in range(N)]

#         def lengthOfLISR(curr, prev):
#             nonlocal dp, N
#             if curr >= N: return 0
#             if dp[curr][prev+1] is not None: return dp[curr][prev+1]
#             c1 = 0
#             if prev == -1 or nums[prev] < nums[curr]:
#                 c1 = 1 + lengthOfLISR(curr+1, curr)

#             c2 = lengthOfLISR(curr+1, prev)
#             dp[curr][prev+1] = max(c1, c2)
#             return dp[curr][prev+1]

#         return lengthOfLISR(0, -1)
