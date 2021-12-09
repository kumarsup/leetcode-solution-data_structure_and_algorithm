class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L1, L2 = len(nums1), len(nums2)
        arr = sorted(nums1 + nums2)
        n = len(arr)

        if n % 2 == 1:
            m = n // 2
            return arr[m]

        if n % 2 == 0:
            m1, m2 = (n - 1) // 2, (n + 1) // 2
            return (arr[m1] + arr[m2]) / 2