class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        split = list(word)

        left, right = 0, word.index(ch)

        while left <= right:
            tmp = word[left]
            split[left] = split[right]
            split[right] = tmp
            left += 1
            right -= 1
            
        return ''.join(split)