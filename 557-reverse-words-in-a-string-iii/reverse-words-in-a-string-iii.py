class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ans = ''
        for w in range(len(arr)):
            for c in range(len(arr[w]) - 1,-1,-1):
                ans += arr[w][c]
            
            if w == len(arr) - 1:
                break
            ans += ' '

        return ans

