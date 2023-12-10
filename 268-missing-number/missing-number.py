class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        __set = set(nums)

        for i in range(-1, len(nums)):
            if i + 1 not in __set:
                return i + 1
        
        return -1