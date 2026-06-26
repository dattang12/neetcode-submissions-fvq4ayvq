from functools import lru_cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(maxsize=None)
        def dfs(node):          # ← lru_cache decorates this function
            if not node:
                return 0

            res = node.val
            if node.left:
                res += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                res += dfs(node.right.left) + dfs(node.right.right)

            res = max(res, dfs(node.left) + dfs(node.right))
            return res
        
        return dfs(root)