class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
      left_total = ans = 0
      total = sum(nums)
      for i in range(len(nums) - 1):
        left_total += nums[i]
        right_total = total - left_total
        if left_total >= right_total:
          ans += 1
      return ans