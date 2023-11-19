class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        bank = dict()
        for i, el in enumerate(nums):
            if el in bank: return [bank[el],i]
            else:
                pair = target - el
                bank[pair] = i
         
