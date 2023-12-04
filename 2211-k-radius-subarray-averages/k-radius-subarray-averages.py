class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        #n = 1
        diameter = 2 * k + 1
        diameter_sum = 0

        if n < diameter:
            return ans
            
        for i in range(diameter):
            diameter_sum += nums[i]   
        
        ans[k] = diameter_sum // diameter

        for i in range(k+1,n - k):
            left = i - k - 1
            right = i + k
            diameter_sum += nums[right] - nums[left]
            ans[i] = diameter_sum // diameter

        return ans

