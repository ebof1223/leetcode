class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map to store indices of elements
        index_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the difference between target and current element
            diff = target - num
            
            # Check if the difference is in the hash map
            if diff in index_map:
                # If found, return the indices
                return [index_map[diff], i]
            
            # Otherwise, add the current element and its index to the hash map
            index_map[num] = i
        
        # Return an empty list if no solution is found
        return 