# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0
        self.number_count = [0] * 10
    def dfs(self, node: TreeNode):
        if node is None:
            return
        if node.val is None:
            return
        self.number_count[node.val] += 1
        if not node.left and not node.right:
            odd_count = 0
            for i in range(1,10):
                if (self.number_count[i] % 2) == 1:
                    odd_count += 1
            if odd_count <= 1:
                self.answer += 1
            self.number_count[node.val] -= 1
            return
        self.dfs(node.left)
        self.dfs(node.right)
        self.number_count[node.val] -= 1
        return
    
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.answer