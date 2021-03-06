# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, node: ListNode) -> ListNode:
      head, tail = self.rec_reverseList(node)
      return head
        
    def rec_reverseList(self, node: ListNode):
      if node is None:
        #leaf case
        return None, None
      else:
        head_node, last_node = self.rec_reverseList(node.next)
        print('return item: {}/n {} '.format(head_node, last_node))

        if last_node is not None:
          #it's not leaf | here i'm changing the order
          node.next=None
          last_node.next = node
          print(head_node, node)
          return head_node, node
        else:
          print('last item: {} '.format(node))
          return node, node