from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        curr_prefix = 0 
        ans = 0 

        for i in range(len(nums)):
            curr_prefix += nums[i]
            diff = curr_prefix - k
            if diff in counts:
                ans += counts[diff]

            counts[curr_prefix] += 1
        return ans