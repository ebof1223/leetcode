class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = [''] * len(s)
        
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left].isalpha() and s[right].isalpha():
                temp = s[left] 
                ans[left] = s[right]
                ans[right] = temp 
                left += 1
                right -= 1
            elif not s[left].isalpha():
                ans[left] = s[left]
                left +=1

            elif not s[right].isalpha():
                ans[right] = s[right]
                right -= 1

        return ''.join(ans)