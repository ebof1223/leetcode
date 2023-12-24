class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0] 
        right_sum = [0] 
        ans = []

        for i in range(len(nums) - 1):
            left_sum.append(left_sum[i] + nums[i])
        
        nums.reverse()

        for i in range(len(nums) - 1):
            right_sum.append(right_sum[i] + nums[i])
        
        right_sum.reverse()

        for i in range(len(nums)):
            ans.append(abs(left_sum[i] - right_sum[i]))

        return ans

