'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3: return []
        nums.sort()
        res = []
        mm = {}
        for i in range(1, n):
            l, r = i - 1, i + 1
            while l >= 0 and r < n:
                sumA = nums[l] + nums[i] + nums[r]
                if sumA == 0:
                    if (nums[l], nums[i], nums[r]) not in mm:
                        res.append([nums[l], nums[i], nums[r]])
                        mm[(nums[l], nums[i], nums[r])] = True
                    l -= 1
                    r += 1
                elif sumA > 0:
                    l -= 1
                else:
                    r += 1
        # res.sort()
        return res


#         visited = [False]*length
#         res = []
#         def checkUnique(arr):
#             nonlocal res, length
#             for x in res:
#                 for k in x:
#                     if k in arr
#             return True
#         def backTrack(arr=[]):
#             nonlocal visited, res, length
#             if sum(arr) == 0 and len(arr) == 3:
#                 print(arr)
#                 if not checkUnique(arr):
#                     arr.sort()
#                     res.append(arr[:])
#                 return

#             for i, val in enumerate(nums):
#                 if not visited[i]:
#                     arr.append(val)
#                     visited[i] = True
#                     backTrack(arr)
#                     visited[i] = False
#                     arr.pop()
#         backTrack()
#         return res
