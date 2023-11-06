class Solution:
    def minFlips(self, target: str) -> int:
        count = 0
        current_bit = '0'

        for bit in target:
            if bit != current_bit:
                count += 1
                current_bit = bit

        return count
    
