class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
      l = max_length = 0
      for r in range(len(s)):
        diff = abs(ord(s[r]) - ord(t[r]))
        maxCost -= diff
        if maxCost >= 0:
          max_length = max(max_length, r - l + 1)

        while maxCost < 0:
          diff_left = abs(ord(s[l]) - ord(t[l]))
          maxCost += diff_left
          l +=1
      return max_length
