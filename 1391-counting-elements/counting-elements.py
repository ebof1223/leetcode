class Solution:
    def countElements(self, arr: List[int]) -> int:
        __set__ = set(arr)
        count = 0
        for num in arr:
            if num + 1 in __set__:
                count +=1

        return count
                    
                    
