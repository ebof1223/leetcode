class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      vowels = 'aeiou'
      l = curr_vowel = 0
      for i in range(k):
        if s[i] in vowels:
          curr_vowel += 1
      max_vowel = curr_vowel
      for i in range(k, len(s)):
        if s[i] in vowels:
          curr_vowel += 1
        if s[l] in vowels:
          curr_vowel -= 1
        max_vowel = max(max_vowel, curr_vowel)
        l +=1
      return max_vowel