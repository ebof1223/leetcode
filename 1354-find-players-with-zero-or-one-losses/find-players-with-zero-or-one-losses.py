from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)  
        loss = defaultdict(int)  
        ans = []

        for match in matches:
            win[match[0]] +=1
            loss[match[1]] += 1
        
        return [sorted([n for n in win if n not in loss]), sorted([n for n in loss if loss[n]
        == 1])]

