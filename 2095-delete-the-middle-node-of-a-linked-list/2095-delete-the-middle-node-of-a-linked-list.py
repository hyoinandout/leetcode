# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        n = 1
        while temp.next:
            n += 1
            temp = temp.next
        
        root = ListNode()
        root.next = head
        for _ in range(n//2):
            root = root.next
            
        root.next = root.next.next
        
        return head if n >= 2 else None
        