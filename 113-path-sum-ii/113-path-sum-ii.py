# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        def dfs(node: TreeNode, currentSum: int, targetSum: int, currentPath: List[int]):
            if node:
                currentPath.append(node.val)
                currentSum += node.val
                if node.left:
                    dfs(node.left,currentSum, targetSum, currentPath)
                if node.right:
                    dfs(node.right,currentSum, targetSum, currentPath)
                if node.left is None and node.right is None:
                    if currentSum == targetSum:
                        answer.append(copy.deepcopy(currentPath))
                currentPath.pop(-1)
        dfs(root,0,targetSum,[])
        
        return answer
    
        