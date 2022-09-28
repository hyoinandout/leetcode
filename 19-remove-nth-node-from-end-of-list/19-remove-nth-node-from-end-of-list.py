# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        lengthCounter = head
        while lengthCounter.next:
            length += 1
            lengthCounter = lengthCounter.next
            
        removeNodePointer = head
        for i in range(length - (n + 1)):
            removeNodePointer = removeNodePointer.next
        
        if removeNodePointer.next:
            if n != length:
                removeNodePointer.next = removeNodePointer.next.next
            else:
                head = removeNodePointer.next
        else:
            head = None
        
        return head
            
            