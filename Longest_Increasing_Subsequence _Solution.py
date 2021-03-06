class Solution:

  def lengthOfLIS(self, nums):
    return self.lengthofLIS(nums, -1000000, 0)
  

  def lengthofLIS(self, nums, prev, next_index):
      if next_index == len(nums):
        return 0
      
      taken = 0
      if nums[next_index] > prev:
        taken = 1 + self.lengthofLIS(nums, nums[next_index], next_index + 1)
      
      nottaken = self.lengthofLIS(nums, prev, next_index + 1)
      return max(taken, nottaken)

      