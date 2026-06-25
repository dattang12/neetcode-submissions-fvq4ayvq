# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = 0
        
        def dfs(node):
            nonlocal count, result
            if node is None:
                return
            
            dfs(node.left)          # go left first (smallest values)
            count += 1              # visit current node
            if count == k:          # check if this is the kth
                result = node.val
                return
            dfs(node.right)         # then go right
        
        dfs(root)
        return result

            

        