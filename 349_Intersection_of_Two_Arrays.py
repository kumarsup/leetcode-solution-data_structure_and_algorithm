'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be
unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
'''
'''
GOLANG Solution:
func intersection(nums1 []int, nums2 []int) []int {
    
    mm:= make(map[int]int, len(nums1)+len(nums2))
    var arr []int
    
    for i := 0; i < len(nums1); i++{
        _, ok := mm[nums1[i]]
        if !ok{
            mm[nums1[i]] += 1
        }
    } 
    
    for i := 0; i < len(nums2); i++{ 
        _, ok := mm[nums2[i]]
        if ok{
            mm[nums2[i]] += 1
        }
    }
    
    for  key, value := range mm {
        if value > 1{
            arr = append(arr, key)   
        }
    }
    
    return arr
}
'''


