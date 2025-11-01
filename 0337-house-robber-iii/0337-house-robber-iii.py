class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))