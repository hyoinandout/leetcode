from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        global visited
        global answer
        
        visited = [False] * 200001
        answer = False
        
        def dfs(currentNode: TreeNode, k: int):
            global visited
            global answer
            if currentNode:
                if visited[currentNode.val + 100000]:
                    answer = True
                visited[k-currentNode.val + 100000] = True
                if currentNode.left:
                    dfs(currentNode.left, k)
                if currentNode.right:
                    dfs(currentNode.right, k)
        
        dfs(root,k)
        return answer