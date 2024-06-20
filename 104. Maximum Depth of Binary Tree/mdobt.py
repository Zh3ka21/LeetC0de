# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        else:
            rightDepth = self.maxDepth(root.right)
            leftDepth = self.maxDepth(root.left)
            return 1 + max(leftDepth, rightDepth)

            
root = TreeNode(3)
root.right = TreeNode(20)
root.left = TreeNode(9) 
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


sol = Solution()
print(sol.maxDepth(root))