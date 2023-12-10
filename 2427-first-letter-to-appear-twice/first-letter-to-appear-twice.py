class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hash_map = set()
        for el in s:
            if el in hash_map:
                return el
            
            hash_map.add(el)
            
        return -1
