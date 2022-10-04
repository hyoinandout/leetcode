# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global answer
        answer = False
        
        def dfs(node: TreeNode, currentSum: int, targetSum: int):
            global answer
            currentSum += node.val
            if node.left is None and node.right is None:
                if currentSum == targetSum:
                    answer = True
                return
            
            if node.left:
                dfs(node.left,currentSum,targetSum)
            if node.right:
                dfs(node.right,currentSum,targetSum)
            
            return
        
        if root:
            dfs(root,0,targetSum)
        
        return answer