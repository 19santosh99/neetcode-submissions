# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    result = []    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]
        m = int(len(lists) / 2)

        leftHead = self.mergeKLists(lists[:m])
        rightHead = self.mergeKLists(lists[m:])

        mergedListHead = self.merge(leftHead, rightHead)



        return mergedListHead

    def merge(self, leftHead, rightHead):
        temp = ListNode()
        head = temp

        while leftHead != None and rightHead != None:
            if leftHead.val <= rightHead.val:
                temp.next = leftHead
                leftHead = leftHead.next

            else:
                temp.next = rightHead
                rightHead = rightHead.next
            
            temp = temp.next

        if leftHead:
            temp.next = leftHead

        if rightHead:
            temp.next = rightHead


        return head.next

