# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(node, subNode):
            if not node and not subNode:  # check this FIRST
                return True
            if not node or not subNode:   # then this
                return False
            if node.val != subNode.val:
                return False
            return isSameTree(node.left, subNode.left) and isSameTree(node.right, subNode.right)

        def move(node, subNode):
            if not node:
                return False
            if node.val == subNode.val:
                if isSameTree(node,subNode):
                    return True
            return move(node.left, subNode) or move(node.right, subNode)
        return move(root, subRoot)
            
        