from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        ans = 0
        for num in nums:
            counts[num] +=1

        for num in nums:
            if counts[num] == 1:
                ans = max(ans,num)

        if ans == 0:
            return -1
            
        return ans