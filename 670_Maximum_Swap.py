'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
0 <= num <= 108
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        maxNum, start, end, prev = "0", -1, -1, "0"

        for i in range(len(nums)):
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i] and maxNum < nums[j]:
                    maxNum = nums[j]
                    end = j
                    start = i
            # if maxNum != 0: break
        print(maxNum, start, end)

        if start != -1 and end != -1:
            nums[start], nums[end] = nums[end], nums[start]
        else:
            return num

        value = "".join(nums)
        return int(value)
