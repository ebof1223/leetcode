class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        days = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                last_item = stack.pop()
                dif = i - last_item
                days[last_item] = dif
            stack.append(i)
        return days
                
         
