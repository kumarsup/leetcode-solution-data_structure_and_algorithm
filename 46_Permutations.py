'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        res = []

        def backTrack(val=[], idx=0):
            nonlocal res, visited

            if len(val) == n:
                res.append(val[:])
                return

            for i in range(n):
                if not visited[i]:
                    val.append(nums[i])
                    visited[i] = True
                    backTrack(val, i + 1)
                    visited[i] = False
                    val.pop()

        backTrack(val=[], idx=0)
        return res