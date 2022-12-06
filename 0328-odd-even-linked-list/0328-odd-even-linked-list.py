# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def even_dfs(current_node:ListNode):
            if current_node.next is None:
                return ListNode(val = current_node.val)
            if current_node.next.next is None:
                return ListNode(val = current_node.val)
            return ListNode(current_node.val, even_dfs(current_node.next.next))
        def dfs(current_node:ListNode, even_list:ListNode):
            if current_node.next is None:
                current_node.next = even_list
                return current_node
            if current_node.next.next is None:
                current_node.next = even_list
                return current_node
            return ListNode(val = current_node.val, next = dfs(current_node.next.next, even_list))
        if head:
            if head.next:
                evenList = even_dfs(head.next)
                return dfs(head,evenList)
            else:
                return head
        else:
            return head