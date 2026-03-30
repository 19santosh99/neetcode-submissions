# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Base Case
        if head == None or head.next == None:
            return head

        
        sublist = self.reverseList(head.next)
        
        # Use the existing head.next pointer to find the tail of the reversed sublist
        head.next.next = head
        head.next = None

        return sublist
        