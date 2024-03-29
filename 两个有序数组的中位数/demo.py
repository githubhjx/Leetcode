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
class Solution:
    def findMedianSortedArrays(self, A, B) -> float:
        m = len(A)
        n = len(B)
        if m > n:
            return findMedianSortedArrays(self, B, A)   # 保证 m <= n

        iMin = 0
        iMax = m
        while (iMin <= iMax):
            i = (iMin + iMax) / 2
            j = (m + n + 1) / 2 - i
            if j != 0 and i != m and B[j-1] > A[i]:     # i 需要增大
                iMin = i + 1
            
            elif i != 0 and j != n and A[i-1] > B[j]:   # i 需要减小
                iMax = i - 1
            
            else:  # 达到要求，并且将边界条件列出来单独考虑
                maxLeft = 0
                if i == 0:
                    maxLeft = B[j-1]
                elif j == 0:
                    maxLeft = A[i-1]
                else:
                    maxLeft = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1: 
                    return maxLeft  # 奇数的话不需要考虑右半部分

                minRight = 0
                if i == m:
                    minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(B[j], A[i])

                return (maxLeft + minRight) / 2.0   # 如果是偶数的话返回结果
        return 0
