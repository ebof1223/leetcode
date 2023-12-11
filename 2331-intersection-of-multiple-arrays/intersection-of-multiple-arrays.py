from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)

        for arr in nums:
            for num in arr:
                count[num] += 1
        
        n = len(nums)
        ans = []

        for key in count:
            if count[key] == n:
                ans.append(key)
        return sorted(ans)