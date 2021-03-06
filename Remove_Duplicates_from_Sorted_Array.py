class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev =  nums[1]
        i=0
        while i <= len(nums):
          if prev ==None:
            prev = nums[i]
            i+=1 
          else:
            if prev == nums[i]:
              nums.remove(nums[i])
              #Don't change counter as you will remove an item and the counter just changed
            else:
              prev = nums[i]
              i+=1 
                    
        return nums
          