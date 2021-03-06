# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while True:
          newnode = ListNode() 
          if 10 < l1.val + l2.val:
            decena = 1
          else:
            decena =0
          newnode.val = decena + (l1.val + l2.val)%10
          if prevnode is not None:
            prevnode.next =  newnode
          prevnode = newnode  

          if l1.next is not None:
            l1 = l1.next 
          else:
            notl1 =True
            l1 = ListNode()
            l1.val = 0

          if l2.next is not None:
            l2 = l2.next 
          else:
            notl2 =True
            l2 = ListNode()
            l2.val = 0
            
          if notl1 and notl2:
            break
                      