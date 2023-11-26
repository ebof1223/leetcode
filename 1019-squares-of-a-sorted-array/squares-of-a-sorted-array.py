class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = list()
        while l <= r:
            l_sq = nums[l] ** 2
            r_sq = nums[r] ** 2
            if l_sq < r_sq:
                ans.append(r_sq)
                r -= 1
            else:
                ans.append(l_sq)
                l +=1

        ans.reverse()
        return ans