from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        curr = ans = 0
        for num in nums:
            curr += num
            ans += hash_map[curr - k]
            hash_map[curr] += 1
        return ans

