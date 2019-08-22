"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
"""

# 合并数组，取中位数
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2] + nums1[(len(nums1)//2) - 1]) / 2
        else:
            return nums1[(len(nums1)//2)]

# 递归法，数学容易证明，将两个数组取二分，得到两个中间值，共四段，
# 则两个数组的中位数必然在小的中间值后半段和大的中间值的前半段，递归剩下两段
