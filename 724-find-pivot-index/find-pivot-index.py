class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      pivot = [nums[0]]

      for i in range(1, len(nums)):
        pivot.append( nums[i] + pivot[i - 1])
      
      tot = pivot[-1]

      for i in range(len(pivot)):
        left_sum  = pivot[i] - nums[i]
        right_sum = tot - pivot[i]
        if left_sum == right_sum:
          return i
      
      return -1