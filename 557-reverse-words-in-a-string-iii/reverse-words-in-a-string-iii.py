class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        ans = list()

        for w in range(len(arr)):
            word_arr = list()
            for c in range(len(arr[w]) - 1,-1,-1):
                word_arr.append(arr[w][c])
            
            ans.append(''.join(word_arr))
       

        
        return ' '.join(ans)
