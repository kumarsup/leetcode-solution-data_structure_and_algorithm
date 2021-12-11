'''
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0: return -1
        if n == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        l = 0
        r = n - 1

        while l <= r:
            m = l + r // 2
            if nums[m] == target: return m
            if nums[m] > nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

#         def findPivoteBS(l, r):
#             if l < r:
#                 m = (l + r)//2
#                 if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
#                     return m
#                 elif nums[m] > nums[0]:
#                     return findPivoteBS(m+1, r)
#                 else:
#                     return findPivoteBS(l, m)
#             return -1

#         def findElementBS(l, r):
#             if l <= r:
#                 m = (l + r)//2
#                 print(l, m, r, nums[m])
#                 if nums[m] == target:
#                     return m
#                 elif target > nums[m]:
#                     l = m+1
#                 else:
#                     r = m-1
#             return -1

#         n = len(nums)
#         if n == 0: return -1

#         if n == 1:
#             if nums[0] == target: return 0
#             else: return -1

#         p = findPivoteBS(0, n-1)

#         print("p", p)
#         if p == -1: return findElementBS(0, n-1)
#         if nums[p] == target: return p

#         if nums[p] > target and nums[0] <= target:
#             return findElementBS(0, p)
#         else:
#             return findElementBS(p+1, n-1)