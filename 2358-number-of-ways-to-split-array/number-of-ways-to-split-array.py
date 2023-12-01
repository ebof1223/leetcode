class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
      
      prefix =  [nums[0]]
      for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

      valid = 0
      for i in range(len(prefix) - 1):
        if prefix[i] >= prefix[-1] - prefix[i]:
          valid +=1

      return valid
      