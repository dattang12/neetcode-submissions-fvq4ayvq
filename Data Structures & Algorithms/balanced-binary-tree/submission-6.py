# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True
        
        def checkBalance(node) -> int:
            if node is None:
                return 0        
            leftSide = checkBalance(node.left)
            rightSide = checkBalance(node.right)
            return 1 + max(leftSide, rightSide)

        if abs(checkBalance(root.left) - checkBalance(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)





        