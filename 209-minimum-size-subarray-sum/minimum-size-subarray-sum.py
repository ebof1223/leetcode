class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
      l = curr = min_len = 0
      for r in range(len(nums)):
        curr += nums[r]
        while curr >= target:
          curr_len = r - l + 1
          if min_len == 0:
            min_len = curr_len
          else:
            min_len = min(min_len, curr_len)
          curr -= nums[l]
          l += 1
      return min_len

        