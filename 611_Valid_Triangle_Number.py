'''
Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take
them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Example 2:

Input: nums = [4,2,3,4]
Output: 4


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        nums.sort()
        ans = 0

        for i in range(n - 1, 1, -1):
            c = nums[i]
            start = 0
            end = i - 1
            while start < end:
                if nums[start] + nums[end] > c:
                    ans += end - start
                    end -= 1
                elif nums[start] + nums[end] <= c:
                    start += 1
        return ans

#         def binarySeach(start, end, val):
#             while start<end:
#                 mid = (start+end)//2
#                 if nums[mid] >= val: end = mid-1
#                 else: start = mid+1
#             return start if val <= nums[start] else start+1

#         for i in range(n-2):
#             if nums[i] == 0: continue
#             for j in range(i+1, n-1):
#                 k = i+2
#                 k = binarySeach(k, n-1, nums[i]+nums[j])
#                 count+=(k-j)-1
#         return count
