class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    x, y = 0,0

    while y < len(t) and x < len(s):
      if s[x] == t[y]:
        x += 1
      y += 1

    return x == len(s)
          