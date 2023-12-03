class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
            

        startValue = min(prefix) 
        if startValue > 0:
            return 1
        
        return abs(startValue) + 1
