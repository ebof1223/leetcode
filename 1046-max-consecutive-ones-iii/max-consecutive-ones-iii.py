class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      count = left = _max = 0

      for right in range(len(nums)):
        if nums[right] == 0:
          count+=1
        while count > k:
          if nums[left] == 0:
            count -=1
          left+=1
        _max = max(_max, right - left +1)
        
      return _max


        