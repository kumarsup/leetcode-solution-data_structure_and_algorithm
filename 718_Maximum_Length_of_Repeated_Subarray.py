'''
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]

Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
'''


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #dp = [[None] * len(nums2) for _ in range(len(nums1))]
        #         def recursive(i, j, count):
        #             nonlocal dp
        #             if i >= len(nums1) or j >= len(nums2): return count
        #             if dp[i][j] is not None: return dp[i][j]
        #             if nums1[i] == nums2[j]:
        #                 count  = recursive(i+1, j+1, count+1)
        #             c2 = recursive(i+1, j, 0)
        #             c3 = recursive(i, j+1, 0)
        #             dp[i][j] = max(count, c2, c3)
        #             print(dp)
        #             return dp[i][j]
        #         return recursive(0, 0, 0)

        M, N = len(nums1), len(nums2)
        def maxLengthSubArray(i1, i2, count):
            if i1 >= len(nums1) or i2 >= len(nums2): return count
            if nums1[i1] == nums2[i2]:
                count = maxLengthSubArray(i1 + 1, i2 + 1, count + 1)
            c1 = maxLengthSubArray(i1 + 1, i2, 0)
            c2 = maxLengthSubArray(i1, i2 + 1, 0)
            return max(count, c1, c2)
        return maxLengthSubArray(0, 0, 0)

