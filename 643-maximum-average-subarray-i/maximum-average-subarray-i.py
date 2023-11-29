class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    curr_sum = sum(nums[:k])
    max_avg = curr_sum / k
    for right in range(k, len(nums)):
     curr_sum += nums[right] - nums[right - k]
     max_avg = max(max_avg , curr_sum / k)

    return max_avg