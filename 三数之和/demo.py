"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      '''
      算法思路：最外层控制一个元素的循环，
              内层用双指针，一个从头到尾扫描，另一个从尾到头扫描，判断三个元素的值之和是否为零

      注意：相同的元素需要跳过
      '''
      # 对列表进行排序
      nums.sort()
      res, k = [], 0
      for k in range(len(nums) - 2):
          # 如果出现最小元素为正数，则不存在和为0的情况，直接返回
          if nums[k] > 0:
              break
          # 如果出现第一个元素重复的情况，为避免重复结果，跳过后续执行
          if k > 0 and nums[k] == nums[k - 1]:
              continue
          # 定义接下来的两个元素的双指针
          i, j = k + 1, len(nums) - 1
          while i < j:
              s = nums[k] + nums[i] + nums[j]
              if s < 0:
                  i += 1
                  # 跳过重复元素
                  while i < j and nums[i] == nums[i - 1]:
                      i += 1
              elif s > 0:
                  j -= 1
                  # 跳过重复元素
                  while i < j and nums[j] == nums[j + 1]:
                      j -= 1
              else:
                  # 当出现元素满足条件是，将结果加入到列表
                  res.append([nums[k], nums[i], nums[j]])
                  # 接着更新索引（注意跳过相同元素）
                  i += 1
                  j -= 1
                  while i < j and nums[i] == nums[i - 1]:
                      i += 1
                  while i < j and nums[j] == nums[j + 1]:
                      j -= 1
      return res
