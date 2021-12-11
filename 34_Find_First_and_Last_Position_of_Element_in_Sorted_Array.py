'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1 and nums[0] == target: return [0, 0]

        def binarySearch(isFirst):
            res = -1
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if isFirst:
                        if mid == left or nums[mid - 1] < target: return mid
                        right = mid - 1
                    else:
                        if mid == right or nums[mid + 1] > target: return mid
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        start = binarySearch(True)
        if start == -1: return [-1, -1]
        end = binarySearch(False)

        return [start, end]


'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1 and nums[0] == target: return [0, 0]
        
        def binarySearch(isLeft):
            res = -1
            left, right = 0, len(nums)-1
            while left <= right:    
                mid = (left + right)//2
                if nums[mid] < target:
                    left = mid+1
                elif nums[mid] > target:
                    right = mid-1
                else:
                    res = mid
                    if isLeft:
                        right = mid-1
                    else:
                        left = mid+1
            return res
        start = binarySearch(True)
        if start == -1: return [-1, -1]
        end = binarySearch(False)
        return [start, end]                
'''