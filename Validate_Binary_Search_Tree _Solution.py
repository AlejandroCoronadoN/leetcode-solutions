# Validate Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
      r, minr, maxr= self.isValidBST_rec(root)

      return r
      
    def isValidBST_rec(self, node):
      """ Transverse across the binary tree and checks for each node if it is a
      valid node
      ! The Minimum in the right side must be always bigger than the maximum in the left side
      Args:
          Node (TreeNode): TreeNode class
      """
      if node is None:
        return True, None, None
      else:
        rr, minr, maxr= self.isValidBST_rec(node.right)
        rl, minl, maxl = self.isValidBST_rec(node.left)
        min_list = [node.valid]
        max_list = [node.value]
        if node.right is not None:
          min_list.append(minr)
          max_list.append(maxr)
        if node.left is not None:
          min_list.append(minl)
          max_list.append(maxl)
          
        min_value = min(min_list)
        max_value = max(max_list)
        
        valid_m = self.validate_node(node)
        valid_l = self.validate_node(node.left)
        valid_r = self.validate_node(node.right)
        
        result = valid_l and valid_r and valid_m
        result =  minr >= maxl and maxr >= maxl and minl <= minr and result
        result = minr >= node.val and maxl <= node.val and result 
        result = result and rr and rl
        
        return  result , min_value, max_value
        
        
    
    def validate_node(self, node):
      """Validates right being grater and left being smaller

      Args:
          node ([type]): [description]
      """
      if node is None:
        return True
      if node.right is not None:
        nr_valid = node.val < node.right.val
      else: 
        nr_valid = True
      if node.left is not None:
        nl_valid = node.val > node.left.val 
      else:
        nl_valid = True
        
      return nl_valid and nr_valid 

class Solution:
  def isValidBST(self, root: TreeNode) -> bool:

      def validate(node, low=-math.inf, high=math.inf):
          # Empty trees are valid BSTs.
          if not node:
              return True
          # The current node's value must be between low and high.
          if node.val <= low or node.val >= high:
              return False

          # The left and right subtree must also be valid.
          return (validate(node.right, node.val, high) and
                  validate(node.left, low, node.val))

      return validate(root)