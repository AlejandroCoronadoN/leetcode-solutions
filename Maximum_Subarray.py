import math

class Solution:
  """Given an integer array nums, find the contiguous subarray (containing at least one number) 
  which has the largest sum and return its sum.
  """
  def maxSubArray(self, nums) -> int:
    """ Iterate trough all the numbers in a two nested loops. The first loop will privide
    a pivot that sets the start of the substring. The second loop will iterate again but this
    time we are trying to find the biggest subarray
    
    -105 <= nums[i] <= 105
    Args:
        nums (List[int]): [description]

    Returns:
        int: [description]
    """
    maxsub = -10000000
    i = 0
    solutions = self.create_matrix(nums)
    if len(nums)==1:
      return nums[0]
    while i <= len(nums) -1:
      j=i
      while j <= len(nums)-1:
        sum_ij = solutions[i][j]
        if sum_ij > maxsub:
          maxsub = sum_ij
        j+=1
      i +=1
    return maxsub
  
  def substring_sum(self, nums, i, j):
    sum_ij = 0
    for x in range(i, j+1):
      sum_ij += nums[x]
    return sum_ij
  
  def substring_sum(self, nums, i, j):
    
    
    sum_ij = 0
    for x in range(i, j+1):
      sum_ij += nums[x]
    return sum_ij
  
  def create_matrix(self, nums):
    matrix = {}
    i = 0 
    while i <= len(nums)-1:
      matrix[i] ={}
      j=i
      while j <= len(nums)-1:
        #print('{} {}'.format(i,j))
        if i==j:
          matrix[i][j] =  nums[j]
        else:          
          matrix[i][j] =  matrix[i][j-1] + nums[j]
        j+=1
      i+=1
    return matrix
        
def master_fun(nums):
  if len(nums) == 1:
    return nums[0], 'both'
  else:
    
    left, lp = master_fun(nums[0: math.floor(len(nums)/2)])
    right, rp = master_fun(nums[math.floor(len(nums)/2):len(nums)] )
    
    if left + right > right and left + right  > left:
      if lp != 'left' and rp != 'right': 
        return left+ right, 'both'
        
    if right > left:
      return right, rp
    if left >= right:
      return left, lp
    
class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)
master_fun([1,-3,3,-6,1,1,1,1,1])